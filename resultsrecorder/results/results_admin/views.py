from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from resultsrecorder.utils.forms import emit_errors
from resultsrecorder.elections.models import Election

from .forms import ConfirmForm

@login_required
def view(request, election_ident, post_ident):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)

    return render(request, 'results/admin/view.html', {
        'post': post,
        'election': election,
    })

@require_POST
@login_required
def confirm(request, election_ident, post_ident, result_set_id):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)
    result_set = get_object_or_404(post.result_sets, pk=result_set_id)

    form = ConfirmForm(request.POST, instance=result_set)

    if form.is_valid():
        form.save(request)
        messages.success(request, "Result set confirmed.")
    else:
        emit_errors(request, form)

    return redirect('elections:post', election.ident, post.ident)

@require_POST
@login_required
def delete(request, election_ident, post_ident, result_set_id):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)
    result_set = get_object_or_404(post.result_sets, pk=result_set_id)

    result_set.delete()

    messages.success(request, "Result set deleted.")

    return redirect('elections:post', election.ident, post.ident)

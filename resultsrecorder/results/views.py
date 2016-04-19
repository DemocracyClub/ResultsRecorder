from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from resultsrecorder.elections.models import Election

from .forms import ResultSetForm

@login_required
def submit(request, election_ident, post_ident):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)

    if request.method == 'POST':
        form = ResultSetForm(post, request.POST)

        if form.is_valid():
            form.save(request.user)
            messages.success(request, "Submitted!")

            return redirect('elections:post', election.ident, post.ident)

    else:
        form = ResultSetForm(post)

    return render(request, 'results/submit.html', {
        'post': post,
        'form': form,
        'election': election,
    })

@login_required
def results(request, election_ident, post_ident):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)

    return render(request, 'results/results.html', {
        'post': post,
        'election': election,
    })

@require_POST
@login_required
def verify(request, election_ident, post_ident, result_set_id):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)
    result_set = get_object_or_404(post.result_sets, pk=result_set_id)

    if post.result_sets.filter(is_verified=True).exists():
        messages.error(request, "A result set for this post already exists.")
    else:
        result_set.is_verified = True
        result_set.save()

        messages.success(request, "Result set verified.")

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

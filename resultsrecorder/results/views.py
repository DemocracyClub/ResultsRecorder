from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from resultsrecorder.elections.models import Election

from .forms import ResultSetForm

def submit(request, election_ident, post_ident):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)

    if request.method == 'POST':
        form = ResultSetForm(post, request.POST)

        if form.is_valid():
            form.save(request)
            messages.success(request, "Submitted!")

            return redirect('elections:post', election.ident, post.ident)

    else:
        form = ResultSetForm(post)

    return render(request, 'results/submit.html', {
        'post': post,
        'form': form,
        'election': election,
    })

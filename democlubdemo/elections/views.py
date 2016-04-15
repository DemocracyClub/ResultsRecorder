from django.shortcuts import render, get_object_or_404

from .models import Election

def view(request, election_ident):
    election = get_object_or_404(Election, ident=election_ident)

    return render(request, 'elections/view.html', {
        'election': election,
    })

def post(request, election_ident, post_ident):
    election = get_object_or_404(Election, ident=election_ident)
    post = get_object_or_404(election.posts, ident=post_ident)
    result_set = post.result_sets.filter(is_verified=True).first()

    return render(request, 'elections/post.html', {
        'post': post,
        'election': election,
        'result_set': result_set,
    })

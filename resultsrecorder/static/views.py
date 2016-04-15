from django.shortcuts import render

from resultsrecorder.elections.models import Election

def landing(request):
    elections = Election.objects.all()

    return render(request, 'static/landing.html', {
        'elections': elections,
    })

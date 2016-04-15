from django.shortcuts import render

from democlubdemo.elections.models import Election

def landing(request):
    elections = Election.objects.all()

    return render(request, 'static/landing.html', {
        'elections': elections,
    })

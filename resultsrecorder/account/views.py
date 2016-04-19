from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect, render

from resultsrecorder.utils.decorators import logout_required

from .forms import LoginForm

@logout_required
def login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            form.login()

            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
        'form': form,
    })

def logout(request):
    if request.method == 'POST' or not request.user.is_authenticated():
        auth.logout(request)
        return redirect('static:landing')

    return render(request, 'account/logout.html')

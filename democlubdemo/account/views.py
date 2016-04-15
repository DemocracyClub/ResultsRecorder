from django.contrib import auth
from django.shortcuts import redirect, render

from democlubdemo.utils.decorators import logout_required

@logout_required
def login(request):
    return redirect('social:begin', 'twitter')

def logout(request):
    if request.method == 'POST' or not request.user.is_authenticated():
        auth.logout(request)
        return redirect('static:landing')

    return render(request, 'account/logout.html')

from django.conf import settings
from django.contrib import auth
from django.utils.http import is_safe_url

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(auth.forms.AuthenticationForm):
    def login(self):
        user = self.get_user()
        request = self.request

        redirect_to = request.POST.get(
            auth.REDIRECT_FIELD_NAME,
            request.GET.get(auth.REDIRECT_FIELD_NAME, ''),
        )

        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        auth.login(request, user)

        return redirect_to

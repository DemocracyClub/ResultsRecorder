from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(auth.forms.AuthenticationForm):
    def login(self):
        user = self.get_user()

        auth.login(self.request, user)

        return user

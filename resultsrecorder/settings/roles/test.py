from local import *

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': ':memory:',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

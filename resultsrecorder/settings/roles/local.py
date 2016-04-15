from os.path import abspath, dirname, join

def base_dir(*xs):
    return join(dirname(dirname(dirname(dirname(abspath(__file__))))), *xs)

DEBUG = True
ADMINS = ()

SITE_URL = 'http://127.0.0.1:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'resultsrecorder',
        'ATOMIC_REQUESTS': True,
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

MEDIA_URL = '/storage/'
MEDIA_ROOT = base_dir('storage')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

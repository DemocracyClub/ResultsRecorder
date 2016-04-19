import copy

from os.path import abspath, dirname, join

from django.utils.log import DEFAULT_LOGGING

from apps import *
from setup_warnings import *

BASE_DIR = '/usr/share/python/resultsrecorder'

# Fallback to relative location
if not __file__.startswith(BASE_DIR):
    BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))

DEBUG = False

ADMINS = (
    ('Chris Lamb', 'chris@chris-lamb.co.uk'),
)
MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ('*',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'resultsrecorder',
        'USER': 'resultsrecorder',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = (join(BASE_DIR, 'media'),)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'staticfiles_dotd.finders.DotDFinder',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        join(BASE_DIR, 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'resultsrecorder.utils.context_processors.settings_context',
        ],
        'builtins': [
            'django.contrib.staticfiles.templatetags.staticfiles',
        ],
    },
}]

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django_keyerror.middleware.KeyErrorMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'resultsrecorder.urls'

SECRET_KEY = 'overriden-in-production'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SESSION_COOKIE_AGE = 86400 * 365 * 10
SESSION_COOKIE_HTTPONLY = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'resultsrecorder',
    }
}

SITE_URL = 'overriden-in-production'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

SERVER_EMAIL = 'overriden-in-production'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

FONTS_ENABLED = True

BROKER_URL = 'redis://localhost:6379/0'

AKISMET_KEY = 'overriden-in-production'

KEYERROR_SECRET_KEY = 'private'

STATICFILES_DOTD_RENDER_FN = 'resultsrecorder.debug.utils.render_file'

SLACK_TOKEN = 'overriden-in-production'
SLACK_CHANNEL = '#resultsrecorder'
SLACK_USERNAME = 'resultsrecorder'

# Always log to the console, even in production (ie. gunicorn)
LOGGING = copy.deepcopy(DEFAULT_LOGGING)
LOGGING['handlers']['console']['filters'] = []


# Social auth #################################################################

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_DEFAULT_BACKEND = 'twitter'

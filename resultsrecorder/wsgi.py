"""
WSGI config for resultsrecorder project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resultsrecorder.settings')

application = get_wsgi_application()

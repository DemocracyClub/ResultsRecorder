from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from . import views

urlpatterns = (
    url(r'^media/(?P<path>.*)$', views.media),
    url(r'^404$', views.http404,
        name='http-404'),
    url(r'^500$', views.http500,
        name='http-500'),

    url(r'^storage/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
)

if not settings.DEBUG:
    urlpatterns = ()

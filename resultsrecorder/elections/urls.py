from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^elections/(?P<election_ident>[^/]+)$', views.view,
        name='view'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)$', views.post,
        name='post'),
)

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results$', views.view,
        name='view'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results/(?P<result_set_id>\d+)/confirm$', views.confirm,
        name='confirm'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results/(?P<result_set_id>\d+)/delete$', views.delete,
        name='delete'),
)

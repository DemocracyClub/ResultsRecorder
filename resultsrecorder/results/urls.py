from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/submit$', views.submit,
        name='submit'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results$', views.results,
        name='results'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results/(?P<result_set_id>\d+)/verify$', views.verify,
        name='verify'),
    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/results/(?P<result_set_id>\d+)/delete$', views.delete,
        name='delete'),
)

from django.conf.urls import url, include

from . import views

urlpatterns = (
    url(r'', include('resultsrecorder.results.results_admin.urls',
        namespace='admin')),

    url(r'^elections/(?P<election_ident>[^/]+)/(?P<post_ident>[^/]+)/submit$', views.submit,
        name='submit'),
)

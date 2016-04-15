from django.conf.urls import url, include

urlpatterns = (
    url(r'', include('resultsrecorder.account.urls',
        namespace='account')),
    url(r'', include('resultsrecorder.debug.urls',
        namespace='debug')),
    url(r'', include('resultsrecorder.elections.urls',
        namespace='elections')),
    url(r'', include('resultsrecorder.results.urls',
        namespace='results')),
    url(r'', include('resultsrecorder.static.urls',
        namespace='static')),

    url(r'', include('social.apps.django_app.urls',
        namespace='social')),
)

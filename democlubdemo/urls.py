from django.conf.urls import url, include

urlpatterns = (
    url(r'', include('democlubdemo.account.urls',
        namespace='account')),
    url(r'', include('democlubdemo.debug.urls',
        namespace='debug')),
    url(r'', include('democlubdemo.elections.urls',
        namespace='elections')),
    url(r'', include('democlubdemo.results.urls',
        namespace='results')),
    url(r'', include('democlubdemo.static.urls',
        namespace='static')),

    url(r'', include('social.apps.django_app.urls',
        namespace='social')),
)

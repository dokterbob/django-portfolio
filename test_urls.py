from django.conf.urls import patterns, include


urlpatterns = patterns('',
    (r'^portfolio/', include('portfolio.urls')),
)

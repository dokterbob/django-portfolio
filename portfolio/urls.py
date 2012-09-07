from django.conf.urls import patterns

from surlex.dj import surl

from .views import ArtworkDetailView, ArtworkListView


urlpatterns = patterns('',
    surl(r'^artworks/$', ArtworkListView.as_view()),
    surl(r'^artworks/<id:#>/$', ArtworkDetailView.as_view()),
)

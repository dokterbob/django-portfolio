from django.conf.urls import patterns

from surlex.dj import surl

from .views import (
    ArtworkDetailView, ArtworkListView,
    CollectionListView, CollectionDetailView
)


urlpatterns = patterns('',
    surl(r'^collections/$', CollectionListView.as_view()),
    surl(r'^collections/<slug:s>/', CollectionDetailView.as_view()),
    surl(r'^artworks/$', ArtworkListView.as_view()),
    surl(r'^artworks/<id:#>/$', ArtworkDetailView.as_view())
)

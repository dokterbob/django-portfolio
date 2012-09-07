from django.views.generic import ListView, DetailView

from .models import Artwork, Picture, Category, Collection


class ArtworkViewBase(object):
    model = Artwork


class ArtworkDetailView(ArtworkViewBase, DetailView):
    pass


class ArtworkListView(ArtworkViewBase, ListView):
    pass


class CollectionViewBase(object):
    model = Collection


class CollectionDetailView(CollectionViewBase, DetailView):
    pass


class CollectionListView(CollectionViewBase, ListView):
    pass

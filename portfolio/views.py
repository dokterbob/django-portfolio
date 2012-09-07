from django.views.generic import ListView, DetailView

from .models import Artwork, Picture, Category


class ArtworkViewBase(object):
    model = Artwork


class ArtworkDetailView(ArtworkViewBase, DetailView):
    pass


class ArtworkListView(ArtworkViewBase, ListView):
    pass

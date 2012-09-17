from django.views.generic import ListView, DetailView

from .models import Artwork, Category, Collection


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


class CategoryViewBase(object):
    model = Category


class CategoryDetailView(CategoryViewBase, DetailView):
    pass


class CategoryListView(CategoryViewBase, ListView):
    pass

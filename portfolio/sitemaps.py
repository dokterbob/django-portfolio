from django.contrib.sitemaps import Sitemap

from .models import Artwork, Collection, Category


class ArtworkSitemap(Sitemap):
    def items(self):
        return Artwork.objects.all()

    def lastmod(self, obj):
        return obj.modified


class CollectionSitemap(Sitemap):
    def items(self):
        return Collection.objects.all()


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


portfolio_sitemaps = {
    'artworks': ArtworkSitemap,
    'collections': CollectionSitemap,
    'categories': CategorySitemap
}

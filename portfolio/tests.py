from django.test import TestCase

from .models import Artwork, Category, Collection, Picture


class PortfolioTestBase(TestCase):
    def create_category(self):
        """ Create Category such that it can be saved, but don't save it. """

        obj = Category()

        return obj

    def create_collection(self):
        """ Create collection such that it can be saved, but don't save. """

        obj = Collection()

        return obj


    def create_artwork(self, collection=None):
        """ Create artwork such that it can be saved - but don't save. """

        if not collection:
            collection = self.create_collection()
            collection.save()

        obj = Artwork(collection=collection)
        obj.save()

        return obj


class ArtworkTests(PortfolioTestBase):
    """ Tests for Artworks. """

    def test_create(self):
        """ Create and save Artwork. """

        artwork = self.create_artwork()
        artwork.save()


class CategoryTests(PortfolioTestBase):
    """ Tests for Categories. """

    def test_create(self):
        """ Create and save Category. """

        category = self.create_category()
        category.save()


class CollectionTests(PortfolioTestBase):
    """ Tests for Collections. """

    def test_create(self):
        """ Create and save Collection. """

        collection = self.create_collection()
        collection.save()

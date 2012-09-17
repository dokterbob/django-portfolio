from django.test import TestCase

from .models import Artwork, Category, Collection, Picture


class PortfolioTestBase(TestCase):
    def _get_random_slug(self):
        """ Generate a random slug. """

        import uuid

        return str(uuid.uuid4().hex)[:30]

    def get_unique_slug(self, model, slug_field='slug'):
        """ Set slug to unique value. """

        slug = self._get_random_slug()
        while model.objects.filter(**{slug_field: slug}).exists():
            slug = self._get_random_slug()

        return slug


    def create_category(self, slug=None, title='Test category'):
        """ Create Category such that it can be saved, but don't save it. """

        if not slug:
            slug = self.get_unique_slug(Category)

        obj = Category(slug=slug, title=title)

        return obj

    def create_collection(self, slug=None, title='Test collection'):
        """ Create collection such that it can be saved, but don't save. """

        if not slug:
            slug = self.get_unique_slug(Category)

        obj = Collection(slug=slug, title=title)

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

        obj = self.create_artwork()
        unicode(obj)
        obj.save()

    def test_detailview(self):
        """ Test requesting the object. """

        obj = self.create_artwork()
        obj.save()

        url = obj.get_absolute_url()
        self.assertTrue(url)

        # Make sure the slug is in there
        self.assertIn(str(obj.pk), url)

        # Attempt request
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # The project title should be in the page, somewhere
        self.assertContains(response, obj.title)


class CategoryTests(PortfolioTestBase):
    """ Tests for Categories. """

    def test_create(self):
        """ Create and save Category. """

        obj = self.create_category()
        unicode(obj)
        obj.save()

    def test_detailview(self):
        """ Test requesting the object. """

        obj = self.create_category()
        obj.save()

        url = obj.get_absolute_url()
        self.assertTrue(url)

        # Make sure the slug is in there
        self.assertIn(str(obj.slug), url)

        # Attempt request
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # The project title should be in the page, somewhere
        self.assertContains(response, obj.title)


class CollectionTests(PortfolioTestBase):
    """ Tests for Collections. """

    def test_create(self):
        """ Create and save Collection. """

        obj = self.create_collection()
        unicode(obj)
        obj.save()

    def test_detailview(self):
        """ Test requesting the object. """

        obj = self.create_category()
        obj.save()

        url = obj.get_absolute_url()
        self.assertTrue(url)

        # Make sure the slug is in there
        self.assertIn(str(obj.slug), url)

        # Attempt request
        response = self.client.get(url)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # The project title should be in the page, somewhere
        self.assertContains(response, obj.title)

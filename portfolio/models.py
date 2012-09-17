from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

from sorl.thumbnail import ImageField


class Category(models.Model):
    """ Categorization for works. """

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """ Get URL for object. """

        return ('category_detail', (), {
            'slug': self.slug
        })


class Collection(Sortable):
    """ A collection of artworks. """

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """ Get URL for object. """

        return ('collection_detail', (), {
            'slug': self.slug
        })


class Artwork(Sortable):
    """ Piece of art. """

    collection = models.ForeignKey(Collection)

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    categories = models.ManyToManyField(Category, null=True, blank=True)

    class Meta(Sortable.Meta):
        verbose_name = _('artwork')
        verbose_name_plural = _('artworks')

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """ Get URL for object. """

        return ('artwork_detail', (), {
            'pk': str(self.pk)
        })


class Picture(Sortable):
    """ Picture of an artwork. """

    artwork = models.ForeignKey(Artwork)

    title = models.CharField(_('title'), max_length=255, blank=True)
    image = ImageField(upload_to='portfolio/pictures')

    class Meta(Sortable.Meta):
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')

    def __unicode__(self):
        """ Unicode representation for object. """
        title = self.title or self.pk

        return _(u"%(artwork)s: %(title)s") % {
            'artwork': unicode(self.artwork),
            'title': title
        }

import logging
logger = logging.getLogger(__name__)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

from sorl.thumbnail import ImageField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created" and
    "modified" fields, borrowed from django_extensions.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class Category(Sortable):
    """ Categorization for works. """

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta(Sortable.Meta):
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

    class Meta(Sortable.Meta):
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


class Artwork(Sortable, TimeStampedModel):
    """ Piece of art. """

    collection = models.ForeignKey(Collection, related_name='artworks')

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    categories = models.ManyToManyField(Category,
        related_name='artworks', null=True, blank=True
    )

    class Meta(Sortable.Meta):
        verbose_name = _('work')
        verbose_name_plural = _('works')

    def __unicode__(self):
        """ Unicode representation for object. """
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """ Get URL for object. """

        return ('artwork_detail', (), {
            'pk': str(self.pk)
        })

    def get_default_picture(self):
        """ By default, get the first picture for this Artwork or None. """
        qs = self.pictures.all()

        try:
            return qs[0]
        except IndexError:
            logger.warn('No (default) picture available for %s', self)
            return None


class Picture(Sortable):
    """ Picture of an artwork. """

    artwork = models.ForeignKey(Artwork, related_name='pictures')

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

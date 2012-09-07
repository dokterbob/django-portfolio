from django.db import models
from django.utils.translation import ugettext_lazy as _
from adminsortable.models import Sortable

from sorl.thumbnail import ImageField


class Category(models.Model):
    """ Categorization for works. """

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), db_index=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.title


class Artwork(models.Model):
    """ Piece of art. """

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = _('artwork')
        verbose_name_plural = _('artworks')

    def __unicode__(self):
        return self.title


class Picture(Sortable):
    """ Picture of an artwork. """

    artwork = models.ForeignKey(Artwork)
    image = ImageField(upload_to='portfolio/pictures')

    class Meta(Sortable.Meta):
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')

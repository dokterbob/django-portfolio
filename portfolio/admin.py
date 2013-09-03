import logging
logger = logging.getLogger(__name__)

import sys

from django.contrib import admin

from adminsortable.admin import SortableStackedInline, SortableAdmin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from multilingual_model.admin import TranslationStackedInline

from .models import (
    Category, CategoryTranslation, Picture,
    Artwork, ArtworkTranslation, Collection, CollectionTranslation
)


class ArtworkInline(SortableStackedInline):
    model = Artwork
    max_num = 0
    can_delete = False
    fields = ['title', ]
    readonly_fields = fields

    def title(self, obj):
        return unicode(obj)


class CollectionTranslationInline(TranslationStackedInline):
    model = CollectionTranslation


class CollectionAdmin(SortableAdmin):
    model = Collection
    inlines = [CollectionTranslationInline, ArtworkInline]


class CategoryTranslationInline(TranslationStackedInline):
    model = CategoryTranslation


class CategoryAdmin(SortableAdmin):
    inlines = [CategoryTranslationInline]
    model = Category


class PictureInline(AdminImageMixin, SortableStackedInline):
    model = Picture
    extra = 1


class ArtworkTranslationInline(TranslationStackedInline):
    model = ArtworkTranslation


class ArtworkAdmin(SortableAdmin):
    model = Artwork
    inlines = [ArtworkTranslationInline, PictureInline]
    filter_horizontal = ['categories']
    list_per_page = 15
    list_display = ('thumbnail', 'title', 'collection')
    list_display_links = list_display
    list_filter = ('collection', 'categories', 'created', 'modified')
    search_fields = (
        'translation__title', 'collection__translation__title',
        'categories__translation__title'
    )
    readonly_fields = ('created', 'modified')

    def title(self, obj):
        return unicode(obj)

    def thumbnail(self, obj):
        thumbnail_format = '100x100'
        picture = obj.get_default_picture()

        if picture:
            try:
                thumb = get_thumbnail(
                    picture.image, thumbnail_format, crop='center'
                )

                return '<img src="%s" width="%s" height="%s" alt="%s"/>' \
                    % (thumb.url,  thumb.width, thumb.height, obj.title)
            except Exception:
                logger.error('Admin list thumbnail failed.', exc_info=sys.exc_info())
        return ''
    thumbnail.allow_tags = True


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)

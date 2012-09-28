from django.contrib import admin

from adminsortable.admin import SortableStackedInline, SortableAdmin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from .models import Category, Picture, Artwork, Collection


class ArtworkInline(SortableStackedInline):
    model = Artwork
    max_num = 0
    can_delete = False
    fields = ['title', ]
    readonly_fields = fields


class CollectionAdmin(SortableAdmin):
    model = Collection
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ArtworkInline]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("title",)}


class PictureInline(AdminImageMixin, SortableStackedInline):
    model = Picture
    extra = 1


class ArtworkAdmin(SortableAdmin):
    model = Artwork
    inlines = [PictureInline]
    filter_horizontal = ['categories']
    list_per_page = 15
    list_display = ('thumbnail', 'title', 'collection')
    list_display_links = list_display
    list_filter = ('collection', 'categories')

    def thumbnail(self, obj):
        thumbnail_format = '100x100'
        picture = obj.get_default_picture()

        if picture:
            thumb = get_thumbnail(
                picture.image, thumbnail_format, crop='center'
            )

            return '<img src="%s" width="%s" height="%s" alt="%s"/>' \
                % (thumb.url,  thumb.width, thumb.height, obj.title)

        return ''
    thumbnail.allow_tags = True


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)

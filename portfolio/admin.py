from django.contrib import admin

from adminsortable.admin import SortableStackedInline, SortableAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Category, Picture, Artwork, Collection


class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    prepopulated_fields = {"slug": ("title",)}


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


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)

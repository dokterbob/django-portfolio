from django.contrib import admin

from adminsortable.admin import SortableStackedInline
from sorl.thumbnail.admin import AdminImageMixin

from .models import Category, Picture, Artwork, Collection


class CollectionAdmin(admin.ModelAdmin):
    model = Collection


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class PictureInline(AdminImageMixin, SortableStackedInline):
    model = Picture


class ArtworkAdmin(admin.ModelAdmin):
    model = Artwork


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)

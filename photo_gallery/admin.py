from django.contrib import admin

from .models import *


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category, CategoryAdmin)


class PhotoGalleryAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'draft',
    ]
    list_filter = [
        'created',
        'updated',
        'draft',
        'category__name'
    ]
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = [
        'title',
        'category__name',
        'price'
    ]


admin.site.register(PhotoGallery, PhotoGalleryAdmin)


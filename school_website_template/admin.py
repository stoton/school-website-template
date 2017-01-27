from django.contrib import admin
from .models import WebsitePost, ImageInGallery, Gallery
admin.site.register(WebsitePost)
admin.site.register(ImageInGallery)
admin.site.register(Gallery)


class GalleryImageInline(admin.TabularInline):
    model = ImageInGallery
    extra = 3


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, ]


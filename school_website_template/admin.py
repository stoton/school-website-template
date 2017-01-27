from django.contrib import admin
from .models import WebsitePost, GalleryImage, Gallery
admin.site.register(WebsitePost)
admin.site.register(GalleryImage)
admin.site.register(Gallery)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, ]


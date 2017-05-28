from django.conf.urls import url
from .views import MainPageView, GalleryView, AllGalleriesView, UploadView, WebsitePostCreate, ContactView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^main', MainPageView.as_view(), name="main_page"),
    url(r'^gallery/all', AllGalleriesView.as_view(), name="gallery_view"),
    url(r'^gallery/(?P<pk>\d+)/', GalleryView.as_view(), name="gallery_view"),
    url(r'^gallery/upload', UploadView.as_view(), name='upload_view'),
    url(r'^addPost', WebsitePostCreate.as_view(), name='create_post'),
    url(r'^contact', ContactView.as_view(),name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

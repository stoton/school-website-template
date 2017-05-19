from django.views.generic.list import ListView
from .models import WebsitePost, Gallery
from django.views.generic.edit import CreateView
from .forms import UploadForm, WebsitePostForm

class MainPageView(ListView):
    template_name = 'main_page/main_page.html'
    context_object_name = 'list_of_website_posts'

    def get_queryset(self):
        return WebsitePost.objects.all()[:2]


class GalleryView(ListView):
    template_name = 'gallery/all_of_current_id.html'
    context_object_name = 'list_of_images'

    def get_queryset(self):
        gallery = Gallery.objects.filter(pk=self.kwargs['pk']).get()
        image_list = gallery.image_in_gallery.all()
        return image_list


class AllGalleriesView(ListView):
    template_name = 'gallery/all_galleries.html'
    context_object_name = 'list_of_images'

    def get_queryset(self):
        return Gallery.objects.all()


class UploadView(CreateView):
    model = Gallery
    form_class = UploadForm
    template_name = 'gallery/upload.html'
    success_url = '/all'


class WebsitePostCreate(CreateView):
    model = WebsitePost
    form_class = WebsitePostForm
    template_name = 'website_post/create_website_post.html'
    success_url = '/main'

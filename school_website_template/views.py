from django.views.generic.list import ListView
from .models import WebsitePost, Gallery
from django.views.generic.edit import CreateView
from .forms import UploadForm, WebsitePostForm
from django.template.defaulttags import register
from .configuration import Link


# when we create some views we should add whole configuration into

class MainPageView(ListView):
    model = WebsitePost
    template_name = 'main_page/main_page.html'

    link = Link()

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)
        context['link'] = self.link
        context['list_of_website_posts'] = WebsitePost.objects.all()[:2]
        return context


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery/all_of_current_id.html'
    context_object_name = 'list_of_images'

    link = Link()

    def get_context_data(self, *args, **kwargs):
        gallery = Gallery.objects.filter(pk=self.kwargs['pk']).get()
        image_list = gallery.image_in_gallery.all()
        context = super(GalleryView, self).get_context_data(*args, **kwargs)

        context['link'] = self.link
        context['list_of_images'] = image_list
        return context

    def key(d, key_name):
        return d[key_name]

    key = register.filter('key', key)


class AllGalleriesView(ListView):
    model = Gallery
    template_name = 'gallery/all_galleries.html'

    link = Link()

    def get_context_data(self, *args, **kwargs):
        context = super(AllGalleriesView, self).get_context_data(*args, **kwargs)
        context['link'] = self.link
        context['list_of_images'] = Gallery.objects.all()
        return context


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


class ContactView(ListView):
    model = WebsitePost
    template_name = 'contact.html'
    link = Link()

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        context['link'] = self.link
        return context


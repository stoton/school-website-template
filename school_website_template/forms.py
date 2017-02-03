from __future__ import absolute_import
from django import forms
from multiupload.fields import MultiImageField
from .models import Gallery, GalleryImage, WebsitePost
from ckeditor.fields import RichTextFormField


class UploadForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'author']

    images = MultiImageField(min_num=1, max_num=500, max_file_size=1024*1024*5)

    def save(self, commit=True):
        instance = super(UploadForm, self).save(commit)
        for each in self.cleaned_data['images']:
            GalleryImage.objects.create(image=each, gallery=instance)
        return instance


class WebsitePostForm(forms.ModelForm):

    class Meta:
        model = WebsitePost
        fields = ['content', 'author', 'title', 'category', ]

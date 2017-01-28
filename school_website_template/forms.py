from email.mime import image
from mimetypes import guess_all_extensions

from django import forms
from multiupload.fields import MultiImageField
from .models import Gallery, GalleryImage


class UploadForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'author']

    images = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    def save(self, commit=True):
        instance = super(UploadForm, self).save(commit)
        for each in self.cleaned_data['images']:
            GalleryImage.objects.create(image=each, gallery=instance)

        return instance
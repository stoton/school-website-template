from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('school_website_template.urls', namespace='main')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
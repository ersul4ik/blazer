from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from factories.urls import urlpatterns as factories_patterns


urlpatterns = [
    path('busmordor/', admin.site.urls),
    path('', include(factories_patterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

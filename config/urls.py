from django.contrib import admin
from django.urls import path, include

from factories.urls import urlpatterns as factories_patterns


urlpatterns = [
    path('busmordor/', admin.site.urls),
    path('dashboard/', include(factories_patterns)),
]

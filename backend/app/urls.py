from django.contrib import admin
from django.conf.urls.static import static
from django.urls import re_path
from django.urls import path, include
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('customer.urls')),
    path('api/catalog/', include('catalog.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

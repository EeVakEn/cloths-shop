from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_nested_admin/', include('nested_admin.urls')),

    path('api/catalog/', include('catalog.urls')),
    path('api/customer/', include('customer.urls')),

    # djoser auth
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

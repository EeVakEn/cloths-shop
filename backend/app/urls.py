from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import DictDetail
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/catalog/', include('catalog.urls')),
    path('req/', DictDetail.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api/customer/', include('customer.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

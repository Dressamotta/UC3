
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app02.views import home, Produtos



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # página inicial
    path('', include('app02.urls')),  # inclui as URLs do app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
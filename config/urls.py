from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from desa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.beranda, name='beranda'),
    path('profil/', views.profil, name='profil'),
    path('berita/', views.daftar_berita, name='daftar_berita'),
    path('berita/<int:pk>/', views.detail_berita, name='detail_berita'),
    path('kegiatan/', views.daftar_kegiatan, name='daftar_kegiatan'),
    path('kontak/', views.kontak, name='kontak'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

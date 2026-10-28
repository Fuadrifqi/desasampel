from django.contrib import admin
from .models import ProfilDesa, Berita, Kegiatan

@admin.register(ProfilDesa)
class ProfilDesaAdmin(admin.ModelAdmin):
    list_display = ('nama_desa', 'kecamatan', 'kabupaten', 'diperbarui')

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_publikasi', 'diterbitkan')
    list_filter = ('diterbitkan', 'tanggal_publikasi')
    search_fields = ('judul', 'ringkasan', 'isi')
    list_editable = ('diterbitkan',)

@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tanggal', 'ditampilkan')
    list_filter = ('ditampilkan',)
    search_fields = ('nama', 'deskripsi')

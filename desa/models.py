from django.db import models
from django.utils import timezone

class ProfilDesa(models.Model):
    nama_desa = models.CharField(max_length=150, default='Desa Sejahtera')
    kecamatan = models.CharField(max_length=150, blank=True)
    kabupaten = models.CharField(max_length=150, blank=True)
    sambutan = models.TextField(blank=True)
    sejarah = models.TextField(blank=True)
    visi = models.TextField(blank=True)
    misi = models.TextField(blank=True)
    alamat = models.TextField(blank=True)
    telepon = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    foto_hero = models.ImageField(upload_to='profil/', blank=True, null=True)
    diperbarui = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profil Desa'
        verbose_name_plural = 'Profil Desa'

    def __str__(self):
        return self.nama_desa

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    ringkasan = models.CharField(max_length=300, blank=True)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/', blank=True, null=True)
    tanggal_publikasi = models.DateTimeField(default=timezone.now)
    diterbitkan = models.BooleanField(default=True)

    class Meta:
        ordering = ['-tanggal_publikasi']
        verbose_name_plural = 'Berita'

    def __str__(self):
        return self.judul

class Kegiatan(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    tanggal = models.DateField(blank=True, null=True)
    gambar = models.ImageField(upload_to='kegiatan/', blank=True, null=True)
    ditampilkan = models.BooleanField(default=True)

    class Meta:
        ordering = ['-tanggal']
        verbose_name_plural = 'Kegiatan'

    def __str__(self):
        return self.nama

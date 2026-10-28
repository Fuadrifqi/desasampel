from django.shortcuts import render, get_object_or_404
from .models import ProfilDesa, Berita, Kegiatan

def profil_aktif():
    return ProfilDesa.objects.first()

def beranda(request):
    context = {
        'profil': profil_aktif(),
        'berita_terbaru': Berita.objects.filter(diterbitkan=True)[:3],
        'kegiatan_terbaru': Kegiatan.objects.filter(ditampilkan=True)[:3],
    }
    return render(request, 'desa/beranda.html', context)

def profil(request):
    return render(request, 'desa/profil.html', {'profil': profil_aktif()})

def daftar_berita(request):
    return render(request, 'desa/berita.html', {
        'profil': profil_aktif(),
        'berita_list': Berita.objects.filter(diterbitkan=True),
    })

def detail_berita(request, pk):
    berita = get_object_or_404(Berita, pk=pk, diterbitkan=True)
    return render(request, 'desa/detail_berita.html', {'profil': profil_aktif(), 'berita': berita})

def daftar_kegiatan(request):
    return render(request, 'desa/kegiatan.html', {
        'profil': profil_aktif(),
        'kegiatan_list': Kegiatan.objects.filter(ditampilkan=True),
    })

def kontak(request):
    return render(request, 'desa/kontak.html', {'profil': profil_aktif()})

# Website Profil Desa - Django

Starter project website profil desa dengan landing page responsif, halaman profil, berita, detail berita, kegiatan, kontak, dan Django Admin.

## 1. Persiapan
Pastikan Python sudah terpasang. Buka folder proyek di VS Code, lalu buka terminal.

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 2. Buat database
```powershell
python manage.py makemigrations desa
python manage.py migrate
python manage.py createsuperuser
```

## 3. Jalankan website
```powershell
python manage.py runserver
```
Buka http://127.0.0.1:8000/

## 4. Kelola konten
Buka http://127.0.0.1:8000/admin/ dan login menggunakan akun superuser yang dibuat. Isi Profil Desa, Berita, dan Kegiatan dari panel admin.

## Catatan
- Nama, kecamatan, kabupaten, sejarah, visi, misi, alamat, kontak, berita, dan kegiatan merupakan contoh/isi awal yang perlu disesuaikan.
- Foto berita/kegiatan diunggah lewat Django Admin.
- Gambar hero dan gambar ilustrasi menggunakan URL Unsplash sehingga memerlukan internet untuk dimuat.
- `DEBUG = True` hanya untuk pengembangan lokal. Sebelum deployment, atur `DEBUG = False`, `ALLOWED_HOSTS`, `SECRET_KEY`, static/media hosting, dan konfigurasi keamanan.

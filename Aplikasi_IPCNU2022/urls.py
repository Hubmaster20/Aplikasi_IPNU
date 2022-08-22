"""Aplikasi_IPCNU2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='homekhol')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_IPCNU2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views

from .views import index, HomeView, LogoutView, Data_pimpinan, Tambah_pimpinan, Edit_pimpinan, Hapus_pimpinan, Data_surat, Tambah_surat, Edit_surat, Hapus_surat, Data_anggota, Tambah_anggota, Edit_anggota, Hapus_anggota, Data_kegiatan, Tambah_kegiatan, Edit_kegiatan, Hapus_kegiatan, Data_kegiatan, Tambah_kegiatan, Edit_kegiatan, Hapus_kegiatan, Data_organisasi, Tambah_organisasi, Edit_organisasi, Hapus_organisasi, Data_skretaris, Tambah_skretaris, Edit_skretaris, Hapus_skretaris, Data_bendahara, Tambah_bendahara, Edit_bendahara, Hapus_bendahara, Data_keuangan, Tambah_keuangan, Edit_keuangan, Hapus_keuangan, Data_pengajuan, Tambah_pengajuan, Edit_pengajuan, Hapus_pengajuan, Data_proposal, Tambah_proposal, Edit_proposal, Hapus_proposal, Login_anggota, proses_login, logout_anggota, info_proposal, check_pengajuan, info_kegiatan, info_organisasi, info_saran, Menu_laporan, lp_anggota,lp_organisasi, lp_skretaris, lp_bendahara, lp_pembina, Data_pembina, Tambah_pembina, Edit_pembina, Hapus_pembina, info_pesan, Data_surat_pac, Tambah_surat_pac, Edit_surat_pac, Hapus_surat_pac, Data_organisasi_pac, Tambah_organisasi_pac, Edit_organisasi_pac, Hapus_organisasi_pac, Data_pimpinan_pac, Tambah_pimpinan_pac, Edit_pimpinan_pac, Hapus_pimpinan_pac, Data_skretaris_pac, Tambah_skretaris_pac, Edit_skretaris_pac, Hapus_skretaris_pac, Data_bendahara_pac, Tambah_bendahara_pac, Edit_bendahara_pac, Hapus_bendahara_pac, Data_pengajuan_pac, Tambah_pengajuan_pac, Edit_pengajuan_pac, Hapus_pengajuan_pac, Data_saran_anggota1, Hapus_saran_data, Add_saran_anggota1, Hapus_saran_anggota, info_kegiatan_anggota
from django.contrib import admin
from django.urls import path


urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),
    # info group pesan
    url(r'^info_pesan/$', info_pesan, name="info_pesan"),
    # saran
    url(r'^check_saran/$', Data_saran_anggota1, name="check_saran"),
    url(r'^Add_saran_anggota1/$', Add_saran_anggota1, name="Add_saran_anggota1"),
    url(r'^Hapus_saran_data/(?P<hapus_saran>[0-9]+)$', Hapus_saran_data, name="Hapus_saran_data"),
    # pimpinan
    url(r'^pimpinan/$', Data_pimpinan, name="pimpinan"),
    url(r'^tambah_pimpinan/$', Tambah_pimpinan, name="tambah_pimpinan"),
    url(r'^hapus_pimpinan/(?P<hapus_p>[0-9]+)$', Hapus_pimpinan, name="hapus_pimpinan"),
    url(r'^edit_pimpinan/(?P<id_p>[0-9]+)$', Edit_pimpinan, name="edit_pimpinan"),    
    # surat perintah
    url(r'^surat/$', Data_surat, name="surat"),
    url(r'^tambah_surat/$', Tambah_surat, name="tambah_surat"),
    url(r'^hapus_surat/(?P<hapus_s>[0-9]+)$', Hapus_surat, name="hapus_surat"),
    url(r'^edit_surat/(?P<id_s>[0-9]+)$', Edit_surat, name="edit_surat"),        
    # anggota
    url(r'^anggota/$', Data_anggota, name="anggota"),
    url(r'^tambah_anggota/$', Tambah_anggota, name="tambah_anggota"),
    url(r'^hapus_anggota/(?P<hapus_a>[0-9]+)$', Hapus_anggota, name="hapus_anggota"),
    url(r'^edit_anggota/(?P<id_a>[0-9]+)$', Edit_anggota, name="edit_anggota"),
    # kegiatan
    url(r'^kegiatan/$', Data_kegiatan, name="kegiatan"),
    url(r'^tambah_kegiatan/$', Tambah_kegiatan, name="tambah_kegiatan"),
    url(r'^hapus_kegiatan/(?P<hapus_k>[0-9]+)$', Hapus_kegiatan, name="hapus_kegiatan"),
    url(r'^edit_kegiatan/(?P<id_k>[0-9]+)$', Edit_kegiatan, name="edit_kegiatan"),            
    # organisasi
    url(r'^organisasi/$', Data_organisasi, name="organisasi"),
    url(r'^tambah_organisasi/$', Tambah_organisasi, name="tambah_organisasi"),
    url(r'^hapus_organisasi/(?P<hapus_o>[0-9]+)$', Hapus_organisasi, name="hapus_organisasi"),
    url(r'^edit_organisasi/(?P<id_o>[0-9]+)$', Edit_organisasi, name="edit_organisasi"),
    # skretaris
    url(r'^skretaris/$', Data_skretaris, name="skretaris"),
    url(r'^tambah_skretaris/$', Tambah_skretaris, name="tambah_skretaris"),
    url(r'^hapus_skretaris/(?P<hapus_sk>[0-9]+)$', Hapus_skretaris, name="hapus_skretaris"),
    url(r'^edit_skretaris/(?P<id_sk>[0-9]+)$', Edit_skretaris, name="edit_skretaris"),
    # bendahara
    url(r'^bendahara/$', Data_bendahara, name="bendahara"),
    url(r'^tambah_bendahara/$', Tambah_bendahara, name="tambah_bendahara"),
    url(r'^hapus_bendahara/(?P<hapus_bd>[0-9]+)$', Hapus_bendahara, name="hapus_bendahara"),
    url(r'^edit_bendahara/(?P<id_bd>[0-9]+)$', Edit_bendahara, name="edit_bendahara"),
    # keuangan
    url(r'^keuangan/$', Data_keuangan, name="keuangan"),
    url(r'^tambah_keuangan/$', Tambah_keuangan, name="tambah_keuangan"),
    url(r'^hapus_keuangan/(?P<hapus_ku>[0-9]+)$', Hapus_keuangan, name="hapus_keuangan"),
    url(r'^edit_keuangan/(?P<id_ku>[0-9]+)$', Edit_keuangan, name="edit_keuangan"),
    # pengajuan
    url(r'^pengajuan/$', Data_pengajuan, name="pengajuan"),
    url(r'^tambah_pengajuan/$', Tambah_pengajuan, name="tambah_pengajuan"),
    url(r'^hapus_pengajuan/(?P<hapus_peng>[0-9]+)$', Hapus_pengajuan, name="hapus_pengajuan"),
    url(r'^edit_pengajuan/(?P<id_peng>[0-9]+)$', Edit_pengajuan, name="edit_pengajuan"),
    # proposal
    url(r'^proposal/$', Data_proposal, name="proposal"),
    url(r'^tambah_proposal/$', Tambah_proposal, name="tambah_proposal"),
    url(r'^hapus_proposal/(?P<hapus_pro>[0-9]+)$', Hapus_proposal, name="hapus_proposal"),
    url(r'^edit_proposal/(?P<id_pro>[0-9]+)$', Edit_proposal, name="edit_proposal"),
    # pembina
    url(r'^pembina/$', Data_pembina, name="pembina"),
    url(r'^tambah_pembina/$', Tambah_pembina, name="tambah_pembina"),
    url(r'^hapus_pembina/(?P<hapus_pm>[0-9]+)$', Hapus_pembina, name="hapus_pembina"),
    url(r'^edit_pembina/(?P<id_pm>[0-9]+)$', Edit_pembina, name="edit_pembina"),
    # menu laporan dan hasil laporan
    url(r'^Menu_laporan/$', Menu_laporan, name="Menu_laporan"),
    url(r'^lp_anggota/$', lp_anggota, name="lp_anggota"),
    url(r'^lp_bendahara/$', lp_bendahara, name="lp_bendahara"),
    url(r'^lp_skretaris/$', lp_skretaris, name="lp_skretaris"),
    url(r'^lp_organisasi/$', lp_organisasi, name="lp_organisasi"),
    url(r'^lp_pembina/$', lp_pembina, name="lp_pembina"),
    # ------------------------------------------------------------
    # -----------------INFORMAN ANGGOTA---------------------------
    # login anggota
    url(r'^Login_anggota/$', Login_anggota, name="Login_anggota"),
    url(r'^logout_anggota/$', logout_anggota, name="logout_anggota"),
    url(r'^proses_login/$', proses_login, name="proses_login"),
    # informasi
    url(r'^info_proposal/$', info_proposal, name="info_proposal"),
    url(r'^check_pengajuan/$', check_pengajuan, name="check_pengajuan"),
    url(r'^info_kegiatan/$', info_kegiatan, name="info_kegiatan"),
    url(r'^info_organisasi/$', info_organisasi, name="info_organisasi"),
    url(r'^info_saran/$', info_saran, name="info_saran"),
    url(r'^Hapus_saran_anggota/(?P<hapus_saran_ag>[0-9]+)$', Hapus_saran_anggota, name="Hapus_saran_anggota"),


    # ------------------fitur pac----------------------------------
    # surat perintah pac
    url(r'^surat_pac/$', Data_surat_pac, name="surat_pac"),
    url(r'^tambah_surat_pac/$', Tambah_surat_pac, name="tambah_surat_pac"),
    url(r'^hapus_surat_pac/(?P<hapus_spac>[0-9]+)$', Hapus_surat_pac, name="hapus_surat_pac"),
    url(r'^edit_surat_pac/(?P<id_spac>[0-9]+)$', Edit_surat_pac, name="edit_surat_pac"),        
    # organisasi pac
    url(r'^organisasi_pac/$', Data_organisasi_pac, name="organisasi_pac"),
    url(r'^tambah_organisasi_pac/$', Tambah_organisasi_pac, name="tambah_organisasi_pac"),
    url(r'^hapus_organisasi_pac/(?P<hapus_o>[0-9]+)$', Hapus_organisasi_pac, name="hapus_organisasi_pac"),
    url(r'^edit_organisasi_pac/(?P<id_opac>[0-9]+)$', Edit_organisasi_pac, name="edit_organisasi_pac"),
    # pimpinan pac
    url(r'^pimpinan_pac/$', Data_pimpinan_pac, name="pimpinan_pac"),
    url(r'^tambah_pimpinan_pac/$', Tambah_pimpinan_pac, name="tambah_pimpinan_pac"),
    url(r'^hapus_pimpinan_pac/(?P<hapus_pac>[0-9]+)$', Hapus_pimpinan_pac, name="hapus_pimpinan_pac"),
    url(r'^edit_pimpinan_pac/(?P<id_pac>[0-9]+)$', Edit_pimpinan_pac, name="edit_pimpinan_pac"),    
    # skretaris pac
    url(r'^skretaris_pac/$', Data_skretaris_pac, name="skretaris_pac"),
    url(r'^tambah_skretaris_pac/$', Tambah_skretaris_pac, name="tambah_skretaris_pac"),
    url(r'^hapus_skretaris_pac/(?P<hapus_skpac>[0-9]+)$', Hapus_skretaris_pac, name="hapus_skretaris_pac"),
    url(r'^edit_skretaris_pac/(?P<id_skpac>[0-9]+)$', Edit_skretaris_pac, name="edit_skretaris_pac"),
    # bendahara pac
    url(r'^bendahara_pac/$', Data_bendahara_pac, name="bendahara_pac"),
    url(r'^tambah_bendahara_pac/$', Tambah_bendahara_pac, name="tambah_bendahara_pac"),
    url(r'^hapus_bendahara_pac/(?P<hapus_bdpac>[0-9]+)$', Hapus_bendahara_pac, name="hapus_bendahara_pac"),
    url(r'^edit_bendahara_pac/(?P<id_bdpac>[0-9]+)$', Edit_bendahara_pac, name="edit_bendahara_pac"),
    # pengajuan pac
    url(r'^pengajuan_pac/$', Data_pengajuan_pac, name="pengajuan_pac"),
    url(r'^tambah_pengajuan_pac/$', Tambah_pengajuan_pac, name="tambah_pengajuan_pac"),
    url(r'^hapus_pengajuan_pac/(?P<hapus_peng_pac>[0-9]+)$', Hapus_pengajuan_pac, name="hapus_pengajuan_pac"),
    url(r'^edit_pengajuan_pac/(?P<id_peng_pac>[0-9]+)$', Edit_pengajuan_pac, name="edit_pengajuan_pac"),

    # informasi kegiatan anggota
    url(r'^info_kegiatan_anggota/$', info_kegiatan_anggota, name="info_kegiatan_anggota"),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
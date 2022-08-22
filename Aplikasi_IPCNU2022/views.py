from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login

from .models import Model_pimpinan, Model_surat_perintah, Model_anggota, Model_kegiatan, Model_organisasi1, Model_skretaris, Model_bendahara, Model_keuangan, Model_proposal2, Model_syarat_proposal, Model_saran, Model_pembina
import hashlib


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'login.html',  context)


# admin dapat mengakses semua fitur menu

def HomeView(request):	
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	}
	test_group = Group.objects.get(name="pimpinan_cabang")
	test_kegiatan = Group.objects.get(name="group_kegiatan")
	admin_group = request.user.groups.all()

	template_name = None
	if test_group in admin_group:
		template_name = 'index_pac.html'
	elif test_kegiatan in admin_group:
		template_name = 'index_kegiatan.html'
	else:
		template_name = 'index.html'


	return render(request, template_name,  context)

# informasi kegiatan anggota
def info_kegiatan_anggota(request):		
	data = Model_kegiatan.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'data': data,
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	}
	return render(request, 'Master_kegiatan/data_kegiatan/halaman_kegiatan.html',  context)	
# ------------------

def info_pesan(request):		
	context = {
	'page_title':'info',
	}
	return render(request, 'info.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	
# pimpinan
def Data_pimpinan(request):
	data = Model_pimpinan.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_pimpinan/table.html',  context)	

def Tambah_pimpinan(request):
	if request.method == 'POST':
		Model_pimpinan.objects.create(
			nik = request.POST['nik'],
			Nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			skretaris = request.POST['skretaris'],
			foto = request.FILES['foto'],			
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pimpinan/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_pimpinan/tambah.html',  context)	

def Hapus_pimpinan(request, hapus_p):
	Model_pimpinan.objects.filter(id=hapus_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pimpinan')

def Edit_pimpinan(request, id_p):		
	edit_data = Model_pimpinan.objects.get(id=id_p)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.Nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.skretaris = request.POST.get('skretaris')
			edit_data.foto = request.FILES.get('foto')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pimpinan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pimpinan/edit.html',  context)
# suran
def Data_saran_anggota1(request):
	data = Model_saran.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_saran/saran.html',  context)	
# balas saran
def Add_saran_anggota1(request):
	data_saran = Model_saran.objects.all()
	if 'balas_saran' in request.GET:
		balas_saran=request.GET['balas_saran']
		add_saran_anggota = Model_anggota.objects.filter(id_anggota=balas_saran)
	else:
		add_saran_anggota = Model_anggota.objects.filter(id_anggota=None)

	for tampil in add_saran_anggota:
		id_anggota = tampil.id_anggota
		nama = tampil.nama
		foto = tampil.foto


	if request.method == 'POST':
		Model_saran.objects.create(
			saran = request.POST['saran'],
			id_anggota = request.POST['id_anggota'],
			nama_anggota = request.POST['nama_anggota'],			
			)
		messages.info(request, 'Data Berhasil..')
		return HttpResponseRedirect("/check_saran/")

	context = {	
	'data_saran': data_saran,
	'add_saran_anggota': add_saran_anggota,
	'id_anggota': id_anggota,
	'nama': nama,
	'foto': foto
	}
	return render(request, 'Master_data/data_saran/add_saran.html',  context)	

def Hapus_saran_data(request, hapus_saran):
	Model_saran.objects.filter(id=hapus_saran).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('check_saran')

# surat perintah
def Data_surat(request):
	data = Model_surat_perintah.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_surat_perintah/table.html',  context)	

def Tambah_surat(request):
	select_pimpinan = Model_pimpinan.objects.all()
	if 'cari' in request.GET:
		cari_data=request.GET['cari']
		data = Model_pimpinan.objects.filter(nik=cari_data)
	else:
		data = Model_pimpinan.objects.filter(nik=None)		

	if request.method == 'POST':
		Model_surat_perintah.objects.create(			
			nomor_surat = request.POST['nomor_surat'],
			nama_surat = request.POST['nama_surat'],
			perihal = request.POST['perihal'],
			deskripsi = request.POST['deskripsi'],
			hari = request.POST['hari'],			
			tanggal = request.POST['tanggal'],			
			tempat = request.POST['tempat'],			
			acara = request.POST['acara'],			
			nik = request.POST['nik'],
			nama_pimpinan = request.POST['nama_pimpinan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/surat/")		
	context = {	
	'tambah':'tambah',
	'select_pimpinan': select_pimpinan,
	'data': data,	
	}
	return render(request, 'Master_data/data_surat_perintah/tambah.html',  context)	

def Hapus_surat(request, hapus_s):
	Model_surat_perintah.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('surat')

def Edit_surat(request, id_s):		
	select_pimpinan = Model_pimpinan.objects.all()
	edit_data = Model_surat_perintah.objects.get(id=id_s)
	if request.method == 'POST':					
			edit_data.nomor_surat = request.POST.get('nomor_surat')
			edit_data.nama_surat = request.POST.get('nama_surat')
			edit_data.perihal = request.POST.get('perihal')
			edit_data.deskripsi = request.POST.get('deskripsi')
			edit_data.hari = request.POST.get('hari')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.tempat = request.POST.get('tempat')
			edit_data.acara = request.POST.get('acara')
			edit_data.nik = request.POST.get('nik')
			edit_data.nama_pimpinan = request.POST.get('nama_pimpinan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('surat')

	context = {'edit_data': edit_data,}
	return render(request, 'Master_data/data_surat_perintah/edit.html',  context)
# anggota
def Data_anggota(request):
	data = Model_anggota.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_anggota/table.html',  context)	

def Tambah_anggota(request):
	if request.method == 'POST':
		Model_anggota.objects.create(
			id_anggota = request.POST['id_anggota'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			foto = request.FILES['foto'],			
			jabatan = request.POST['jabatan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/anggota/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_anggota/tambah.html',  context)	

def Hapus_anggota(request, hapus_a):
	Model_anggota.objects.filter(id=hapus_a).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('anggota')

def Edit_anggota(request, id_a):		
	edit_data = Model_anggota.objects.get(id=id_a)
	if request.method == 'POST':		
			edit_data.id_anggota = request.POST.get('id_anggota')
			edit_data.nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.foto = request.FILES.get('foto')
			edit_data.jabatan = request.POST.get('jabatan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('anggota')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_anggota/edit.html',  context)

#data kegiatan
def Data_kegiatan(request):
	data = Model_kegiatan.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_kegiatan/table.html',  context)	

def Tambah_kegiatan(request):
	if request.method == 'POST':
		Model_kegiatan.objects.create(
			id_kegiatan = request.POST['id_kegiatan'],
			nama_kegiatan = request.POST['nama_kegiatan'],
			tempat_kegiatan = request.POST['tempat_kegiatan'],
			waktu = request.POST['waktu'],
			tanggal = request.POST['tanggal'],
			foto = request.FILES['foto'],			
			deskripsi = request.POST['deskripsi'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/kegiatan/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_kegiatan/tambah.html',  context)	

def Hapus_kegiatan(request, hapus_k):
	Model_kegiatan.objects.filter(id=hapus_k).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('kegiatan')

def Edit_kegiatan(request, id_k):		
	edit_data = Model_kegiatan.objects.get(id=id_k)
	if request.method == 'POST':		
			edit_data.id_kegiatan = request.POST.get('id_kegiatan')
			edit_data.nama_kegiatan = request.POST.get('nama_kegiatan')
			edit_data.tempat_kegiatan = request.POST.get('tempat_kegiatan')
			edit_data.waktu = request.POST.get('waktu')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.foto = request.FILES.get('foto')
			edit_data.deskripsi = request.POST.get('deskripsi')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('kegiatan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kegiatan/edit.html',  context)
# organisasi
def Data_organisasi(request):
	data = Model_organisasi1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_organisasi/table.html',  context)	

def Tambah_organisasi(request):
	data = Model_pimpinan.objects.all()
	data_anggota = Model_anggota.objects.all()
	if request.method == 'POST':
		Model_organisasi1.objects.create(
			kode_organisasi = request.POST['kode_organisasi'],
			nama_organisasi = request.POST['nama_organisasi'],
			nama_pimpinan = request.POST['nama_pimpinan'],
			nama_skretaris = request.POST['nama_skretaris'],
			nama_anggota = request.POST['nama_anggota'],
			deskripsi = request.POST['deskripsi'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/organisasi/")		
	context = {	
	'tambah':'tambah',
	'data':data,
	'data_anggota':data_anggota,
	}
	return render(request, 'Master_data/data_organisasi/tambah.html',  context)	

def Hapus_organisasi(request, hapus_o):
	Model_organisasi1.objects.filter(id=hapus_o).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('organisasi')

def Edit_organisasi(request, id_o):		
	data = Model_pimpinan.objects.all()
	data_anggota = Model_anggota.objects.all()
	edit_data = Model_organisasi1.objects.get(id=id_o)
	if request.method == 'POST':		
			edit_data.kode_organisasi = request.POST.get('kode_organisasi')
			edit_data.nama_organisasi = request.POST.get('nama_organisasi')
			edit_data.nama_pimpinan = request.POST.get('nama_pimpinan')
			edit_data.nama_skretaris = request.POST.get('nama_skretaris')
			edit_data.nama_anggota = request.POST.get('nama_anggota')
			edit_data.deskripsi = request.POST.get('deskripsi')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('organisasi')

	context = {'edit_data': edit_data,'data':data,'data_anggota':data_anggota}
	return render(request, 'Master_data/data_organisasi/edit.html',  context)
# skretaris
def Data_skretaris(request):
	data = Model_skretaris.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_skretaris/table.html',  context)	

def Tambah_skretaris(request):
	if request.method == 'POST':
		Model_skretaris.objects.create(
			nik = request.POST['nik'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			foto = request.FILES['foto'],			
			jabatan = request.POST['jabatan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/skretaris/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_skretaris/tambah.html',  context)	

def Hapus_skretaris(request, hapus_sk):
	Model_skretaris.objects.filter(id=hapus_sk).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('skretaris')

def Edit_skretaris(request, id_sk):		
	edit_data = Model_skretaris.objects.get(id=id_sk)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.foto = request.FILES.get('foto')
			edit_data.jabatan = request.POST.get('jabatan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('skretaris')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_skretaris/edit.html',  context)
# bendahara
def Data_bendahara(request):
	data = Model_bendahara.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_bendahara/table.html',  context)	

def Tambah_bendahara(request):
	if request.method == 'POST':
		Model_bendahara.objects.create(
			nik = request.POST['nik'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			foto = request.FILES['foto'],			
			jabatan = request.POST['jabatan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/bendahara/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_bendahara/tambah.html',  context)	

def Hapus_bendahara(request, hapus_bd):
	Model_bendahara.objects.filter(id=hapus_bd).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('bendahara')

def Edit_bendahara(request, id_bd):		
	edit_data = Model_bendahara.objects.get(id=id_bd)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.foto = request.FILES.get('foto')
			edit_data.jabatan = request.POST.get('jabatan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('bendahara')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_bendahara/edit.html',  context)

# keuangan
def Data_keuangan(request):
	data = Model_keuangan.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_keuangan/table.html',  context)	

def Tambah_keuangan(request):
	if request.method == 'POST':
		Model_keuangan.objects.create(
			nomor_keuangan = request.POST['nomor_keuangan'],
			nama_keuangan = request.POST['nama_keuangan'],
			jumlah = request.POST['jumlah'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/keuangan/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_keuangan/tambah.html',  context)	

def Hapus_keuangan(request, hapus_ku):
	Model_keuangan.objects.filter(id=hapus_ku).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('keuangan')

def Edit_keuangan(request, id_ku):		
	edit_data = Model_keuangan.objects.get(id=id_ku)
	if request.method == 'POST':		
			edit_data.nomor_keuangan = request.POST.get('nomor_keuangan')
			edit_data.nama_keuangan = request.POST.get('nama_keuangan')
			edit_data.jumlah = request.POST.get('jumlah')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('keuangan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_keuangan/edit.html',  context)
# pengajuan proposal
def Data_pengajuan(request):
	data = Model_proposal2.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_pengajuan/table.html',  context)	

def Tambah_pengajuan(request):
	select_anggota = Model_anggota.objects.all()
	if request.method == 'POST':
		Model_proposal2.objects.create(
			jenis_proposal = request.POST['jenis_proposal'],
			nama_anggota = request.POST['nama_anggota'],
			tema = request.POST['tema'],
			tujuan_proposal = request.POST['tujuan_proposal'],
			upload_proposal = request.FILES['upload_proposal'],
			status = request.POST['status'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pengajuan/")		
	context = {	
	'tambah':'tambah',
	'select_anggota': select_anggota,
	}
	return render(request, 'Master_data/data_pengajuan/tambah.html',  context)	

def Hapus_pengajuan(request, hapus_peng):
	Model_proposal2.objects.filter(id=hapus_peng).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pengajuan')

def Edit_pengajuan(request, id_peng):		
	select_anggota = Model_anggota.objects.all()
	edit_data = Model_proposal2.objects.get(id=id_peng)
	if request.method == 'POST':		
			edit_data.jenis_proposal = request.POST.get('jenis_proposal')
			edit_data.nama_anggota = request.POST.get('nama_anggota')
			edit_data.tema = request.POST.get('tema')
			edit_data.tujuan_proposal = request.POST.get('tujuan_proposal')
			edit_data.upload_proposal = request.FILES.get('upload_proposal')
			edit_data.status = request.POST.get('status')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pengajuan')

	context = {'edit_data': edit_data, 'select_anggota': select_anggota,}
	return render(request, 'Master_data/data_pengajuan/edit.html',  context)
# syarat proposal
def Data_proposal(request):
	data = Model_syarat_proposal.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_proposal/table.html',  context)	

def Tambah_proposal(request):
	if request.method == 'POST':
		Model_syarat_proposal.objects.create(
			nama_proposal = request.POST['nama_proposal'],
			tema = request.POST['tema'],
			tujuan_proposal = request.POST['tujuan_proposal'],
			upload_proposal = request.FILES['upload_proposal'],
			tanggal = request.POST['tanggal'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/proposal/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_proposal/tambah.html',  context)	

def Hapus_proposal(request, hapus_pro):
	Model_syarat_proposal.objects.filter(id=hapus_pro).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('proposal')

def Edit_proposal(request, id_pro):		
	edit_data = Model_syarat_proposal.objects.get(id=id_pro)
	if request.method == 'POST':		
			edit_data.nama_proposal = request.POST.get('nama_proposal')
			edit_data.tema = request.POST.get('tema')
			edit_data.tujuan_proposal = request.POST.get('tujuan_proposal')
			edit_data.upload_proposal = request.FILES.get('upload_proposal')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('proposal')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_proposal/edit.html',  context)

# data pembina
def Data_pembina(request):
	data = Model_pembina.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_pembina/table.html',  context)	

def Tambah_pembina(request):
	if request.method == 'POST':
		Model_pembina.objects.create(
			nik = request.POST['nik'],
			nama_pembina = request.POST['nama_pembina'],
			bidang = request.POST['bidang'],			
			nohp = request.POST['nohp'],
			alamat = request.POST['alamat'],
			jk = request.POST['jk'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pembina/")		
	context = {	
	'tambah':'tambah',
	}
	return render(request, 'Master_data/data_pembina/tambah.html',  context)	

def Hapus_pembina(request, hapus_pm):
	Model_pembina.objects.filter(id=hapus_pm).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pembina')

def Edit_pembina(request, id_pm):		
	edit_data = Model_pembina.objects.get(id=id_pm)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama_pembina = request.POST.get('nama_pembina')
			edit_data.bidang = request.POST.get('bidang')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.jk = request.POST.get('jk')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pembina')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pembina/edit.html',  context)
# MENU LAPORAN
def Menu_laporan(request):	
	context = {	
	'Menu laporan': 'Menu Laporan',
	}
	return render(request, 'Master_data/Laporan/menu.html',  context)
# lp anggota
def lp_anggota(request):
	data = Model_anggota.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_anggota.html',  context)
# lp organisasi
def lp_organisasi(request):
	data = Model_organisasi1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_organisasi.html',  context)
# lp skretaris
def lp_skretaris(request):
	data = Model_skretaris.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_skretaris.html',  context)
# lp bendahara
def lp_bendahara(request):
	data = Model_bendahara.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_bendahara.html',  context)
# lp pembina
def lp_pembina(request):
	data = Model_pembina.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_pembina.html',  context)
# ------------------------------------------------------------
# -----------------INFORMAN ANGGOTA---------------------------

	# login anggota
def Login_anggota(request):
	data = Model_anggota.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_anggota/login.html',  context)	

def logout_anggota(request):	
	context = {	
	'data': 'logout',
	}
	return render(request, 'Master_anggota/logout.html',  context)	
	# login anggota
def proses_login(request):	
	jumlah = Model_anggota.objects.count()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama
	# check pengajuan proposal
		check_proposal = Model_proposal2.objects.filter(nama_anggota=nama_anggota)			

	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	# hitung jumlah
	'jumlah':jumlah,
	'jumlah_kegiatan':jumlah_kegiatan,
	'check_proposal': check_proposal
	}
	return render(request, 'Master_anggota/index.html',  context)	
# data proposal anggota
def info_proposal(request):
	data_proposal = Model_syarat_proposal.objects.all()	
	
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama
	# proses pengajuan proposal
	if request.method == 'POST':
		Model_proposal2.objects.create(
			jenis_proposal = request.POST['jenis_proposal'],
			nama_anggota = request.POST['nama_anggota'],
			tema = request.POST['tema'],
			tujuan_proposal = request.POST['tujuan_proposal'],
			upload_proposal = request.FILES['upload_proposal'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		# return HttpResponseRedirect("/info_proposal/")

	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	'data_proposal': data_proposal,
	

	}
	return render(request, 'Master_anggota/data_proposal/data_proposal.html',  context)

def check_pengajuan(request):
	data_pengajuan = Model_proposal2.objects.all()	
	
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama	
	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	'data_pengajuan':data_pengajuan,
	

	}
	return render(request, 'Master_anggota/data_proposal/chek_pengajuan.html',  context)
# info kegiatan
def info_kegiatan(request):
	data_kegiatan = Model_kegiatan.objects.all()	
	
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama	
	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	'data_kegiatan':data_kegiatan,
	}
	return render(request, 'Master_anggota/data_kegiatan/table.html',  context)

# organisasi
def info_organisasi(request):
	data_organisasi = Model_organisasi1.objects.all()	
	
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama	
	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	'data_organisasi':data_organisasi,
	}
	return render(request, 'Master_anggota/data_organisasi/table.html',  context)
# saran
def info_saran(request):
	data_saran = Model_saran.objects.all()	
	
	# login
	if 'id_anggota' in request.GET:
		id_anggota=request.GET['id_anggota']
		data = Model_anggota.objects.filter(id_anggota=id_anggota)
	else:
		data = Model_anggota.objects.filter(id_anggota=None)	
	# tampil jenis
	for tampil in data:
		id_anggota = tampil.id_anggota
		jabatan= tampil.jabatan
		foto= tampil.foto
		nohp= tampil.nohp
		nama_anggota = tampil.nama	
	# input saran
	if request.method == 'POST':
		Model_saran.objects.create(
			saran = request.POST['saran'],
			id_anggota = request.POST['id_anggota'],
			nama_anggota = request.POST['nama_anggota'],			
			)
	context = {	
	'id_anggota': id_anggota,
	'jabatan':jabatan,
	'foto': foto,
	'nohp': nohp,
	'data':data,
	'nama_anggota':nama_anggota,
	'data_saran':data_saran,
	}
	return render(request, 'Master_anggota/data_saran/saran.html',  context)

def Hapus_saran_anggota(request, hapus_saran_ag):
	Model_saran.objects.filter(id=hapus_saran_ag).delete()
	return redirect('Login_anggota')


# proses halaman pac
# surat perintah
def Data_surat_pac(request):
	data = Model_surat_perintah.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_surat_perintah/table.html',  context)	

def Tambah_surat_pac(request):
	select_pimpinan = Model_pimpinan.objects.all()
	if 'cari' in request.GET:
		cari_data=request.GET['cari']
		data = Model_pimpinan.objects.filter(nik=cari_data)
	else:
		data = Model_pimpinan.objects.filter(nik=None)		

	if request.method == 'POST':
		Model_surat_perintah.objects.create(			
			nomor_surat = request.POST['nomor_surat'],
			nama_surat = request.POST['nama_surat'],
			perihal = request.POST['perihal'],
			deskripsi = request.POST['deskripsi'],
			hari = request.POST['hari'],			
			tanggal = request.POST['tanggal'],			
			tempat = request.POST['tempat'],			
			acara = request.POST['acara'],			
			nik = request.POST['nik'],
			nama_pimpinan = request.POST['nama_pimpinan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/surat_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	'select_pimpinan': select_pimpinan,
	'data': data,	
	}
	return render(request, 'Master_pac/data_surat_perintah/tambah.html',  context)	

def Hapus_surat_pac(request, hapus_spac):
	Model_surat_perintah.objects.filter(id=hapus_spac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('surat_pac')

def Edit_surat_pac(request, id_spac):		
	select_pimpinan = Model_pimpinan.objects.all()
	edit_data = Model_surat_perintah.objects.get(id=id_spac)
	if request.method == 'POST':					
			edit_data.nomor_surat = request.POST.get('nomor_surat')
			edit_data.nama_surat = request.POST.get('nama_surat')
			edit_data.perihal = request.POST.get('perihal')
			edit_data.deskripsi = request.POST.get('deskripsi')
			edit_data.hari = request.POST.get('hari')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.tempat = request.POST.get('tempat')
			edit_data.acara = request.POST.get('acara')
			edit_data.nik = request.POST.get('nik')
			edit_data.nama_pimpinan = request.POST.get('nama_pimpinan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('surat_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data,
	}
	return render(request, 'Master_pac/data_surat_perintah/edit.html',  context)

# organisasi pac
def Data_organisasi_pac(request):
	data = Model_organisasi1.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_organisasi/table.html',  context)	

def Tambah_organisasi_pac(request):
	data = Model_pimpinan.objects.all()
	data_anggota = Model_anggota.objects.all()
	if request.method == 'POST':
		Model_organisasi1.objects.create(
			kode_organisasi = request.POST['kode_organisasi'],
			nama_organisasi = request.POST['nama_organisasi'],
			nama_pimpinan = request.POST['nama_pimpinan'],
			nama_skretaris = request.POST['nama_skretaris'],
			nama_anggota = request.POST['nama_anggota'],
			deskripsi = request.POST['deskripsi'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/organisasi_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	'data':data,
	'data_anggota':data_anggota,
	}
	return render(request, 'Master_pac/data_organisasi/tambah.html',  context)	

def Hapus_organisasi_pac(request, hapus_opac):
	Model_organisasi1.objects.filter(id=hapus_opac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('organisasi_pac')

def Edit_organisasi_pac(request, id_opac):		
	data = Model_pimpinan.objects.all()
	data_anggota = Model_anggota.objects.all()
	edit_data = Model_organisasi1.objects.get(id=id_opac)
	if request.method == 'POST':		
			edit_data.kode_organisasi = request.POST.get('kode_organisasi')
			edit_data.nama_organisasi = request.POST.get('nama_organisasi')
			edit_data.nama_pimpinan = request.POST.get('nama_pimpinan')
			edit_data.nama_skretaris = request.POST.get('nama_skretaris')
			edit_data.nama_anggota = request.POST.get('nama_anggota')
			edit_data.deskripsi = request.POST.get('deskripsi')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('organisasi_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data,
	'data':data,
	'data_anggota':data_anggota,
	}
	return render(request, 'Master_pac/data_organisasi/edit.html',  context)

# pimpinan pac
def Data_pimpinan_pac(request):
	data = Model_pimpinan.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_pimpinan/table.html',  context)	

def Tambah_pimpinan_pac(request):
	if request.method == 'POST':
		Model_pimpinan.objects.create(
			nik = request.POST['nik'],
			Nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			skretaris = request.POST['skretaris'],
			foto = request.FILES['foto'],			
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pimpinan_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	}
	return render(request, 'Master_pac/data_pimpinan/tambah.html',  context)	

def Hapus_pimpinan_pac(request, hapus_pac):
	Model_pimpinan.objects.filter(id=hapus_pac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pimpinan_pac')

def Edit_pimpinan_pac(request, id_pac):		
	edit_data = Model_pimpinan.objects.get(id=id_pac)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.Nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.skretaris = request.POST.get('skretaris')
			edit_data.foto = request.FILES.get('foto')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pimpinan_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data
	}
	return render(request, 'Master_pac/data_pimpinan/edit.html',  context)

# skretaris
def Data_skretaris_pac(request):
	data = Model_skretaris.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_skretaris/table.html',  context)	

def Tambah_skretaris_pac(request):
	if request.method == 'POST':
		Model_skretaris.objects.create(
			nik = request.POST['nik'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			foto = request.FILES['foto'],			
			jabatan = request.POST['jabatan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/skretaris_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	}
	return render(request, 'Master_pac/data_skretaris/tambah.html',  context)	

def Hapus_skretaris_pac(request, hapus_skpac):
	Model_skretaris.objects.filter(id=hapus_skpac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('skretaris_pac')

def Edit_skretaris_pac(request, id_skpac):		
	edit_data = Model_skretaris.objects.get(id=id_skpac)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.foto = request.FILES.get('foto')
			edit_data.jabatan = request.POST.get('jabatan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('skretaris_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data
	}
	return render(request, 'Master_pac/data_skretaris/edit.html',  context)
# bendahara pac
def Data_bendahara_pac(request):
	data = Model_bendahara.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_bendahara/table.html',  context)	

def Tambah_bendahara_pac(request):
	if request.method == 'POST':
		Model_bendahara.objects.create(
			nik = request.POST['nik'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			foto = request.FILES['foto'],			
			jabatan = request.POST['jabatan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/bendahara_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	}
	return render(request, 'Master_pac/data_bendahara/tambah.html',  context)	

def Hapus_bendahara_pac(request, hapus_bdpac):
	Model_bendahara.objects.filter(id=hapus_bdpac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('bendahara_pac')

def Edit_bendahara_pac(request, id_bd):		
	edit_data = Model_bendahara.objects.get(idpac=id_bdpac)
	if request.method == 'POST':		
			edit_data.nik = request.POST.get('nik')
			edit_data.nama = request.POST.get('nama')
			edit_data.jk = request.POST.get('jk')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.nohp = request.POST.get('nohp')
			edit_data.foto = request.FILES.get('foto')
			edit_data.jabatan = request.POST.get('jabatan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('bendahara_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data
	}
	return render(request, 'Master_pac/data_bendahara/edit.html',  context)

# pengajuan proposal pac
def Data_pengajuan_pac(request):
	data = Model_proposal2.objects.all()
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'data': data,
	}
	return render(request, 'Master_pac/data_pengajuan/table.html',  context)	

def Tambah_pengajuan_pac(request):
	select_anggota = Model_anggota.objects.all()
	if request.method == 'POST':
		Model_proposal2.objects.create(
			jenis_proposal = request.POST['jenis_proposal'],
			nama_anggota = request.POST['nama_anggota'],
			tema = request.POST['tema'],
			tujuan_proposal = request.POST['tujuan_proposal'],
			upload_proposal = request.FILES['upload_proposal'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pengajuan_pac/")		
	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'tambah':'tambah',
	'select_anggota': select_anggota,
	}
	return render(request, 'Master_pac/data_pengajuan/tambah.html',  context)	

def Hapus_pengajuan_pac(request, hapus_peng_pac):
	Model_proposal2.objects.filter(id=hapus_peng_pac).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pengajuan_pac')

def Edit_pengajuan_pac(request, id_peng_pac):		
	select_anggota = Model_anggota.objects.all()
	edit_data = Model_proposal2.objects.get(id=id_peng_pac)
	if request.method == 'POST':		
			edit_data.jenis_proposal = request.POST.get('jenis_proposal')
			edit_data.nama_anggota = request.POST.get('nama_anggota')
			edit_data.tema = request.POST.get('tema')
			edit_data.tujuan_proposal = request.POST.get('tujuan_proposal')
			edit_data.upload_proposal = request.FILES.get('upload_proposal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pengajuan_pac')

	jumlah_kegiatan = Model_kegiatan.objects.count()
	jumlah_pembina = Model_pembina.objects.count()
	jumlah_pengajuan_proposal = Model_proposal2.objects.count()
	context = {
	'page_title':'Home',
	'jumlah_kegiatan':jumlah_kegiatan,
	'jumlah_pembina': jumlah_pembina,
	'jumlah_pengajuan_proposal': jumlah_pengajuan_proposal,
	'edit_data': edit_data, 
	'select_anggota': select_anggota,
	}
	return render(request, 'Master_pac/data_pengajuan/edit.html',  context)
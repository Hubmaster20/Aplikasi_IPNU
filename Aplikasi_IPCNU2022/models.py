from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_pimpinan(models.Model):
	nik	= models.CharField(max_length = 1200)
	Nama	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 25)
	alamat	=models.CharField(max_length = 1250)
	nohp	=models.CharField(max_length = 25)
	skretaris	=models.CharField(max_length = 1250)
	foto	=models.ImageField(upload_to ='Berkas/', null=True)	
	keterangan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nik)

class Model_surat_perintah(models.Model):
	nomor_surat	= models.CharField(max_length = 1200)
	nama_surat	=models.CharField(max_length = 1200)
	perihal	=models.CharField(max_length = 1250)
	deskripsi	=models.CharField(max_length = 1250)
	hari	=models.CharField(max_length = 25)
	tanggal	=models.CharField(max_length = 12)
	tempat	=models.CharField(max_length = 1250)
	acara	=models.CharField(max_length = 1250)
	nik	=models.CharField(max_length = 125)
	nama_pimpinan	=models.CharField(max_length = 1250)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nomor_surat)

class Model_anggota(models.Model):
	id_anggota	= models.CharField(max_length = 1200)
	nama	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 25)
	alamat	=models.CharField(max_length = 1250)
	nohp	=models.CharField(max_length = 25)
	foto	=models.ImageField(upload_to ='Berkas/', null=True)	
	jabatan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama)

class Model_kegiatan(models.Model):
	id_kegiatan	= models.CharField(max_length = 1200)
	nama_kegiatan	=models.CharField(max_length = 1200)
	tempat_kegiatan	=models.CharField(max_length = 25)
	waktu	=models.CharField(max_length = 1250)
	tanggal	=models.CharField(max_length = 25)
	foto	=models.ImageField(upload_to ='Berkas/', null=True)	
	deskripsi	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kegiatan)

class Model_organisasi1(models.Model):
	kode_organisasi	= models.CharField(max_length = 1200)
	nama_organisasi	=models.CharField(max_length = 1200)
	nama_pimpinan	=models.CharField(max_length = 1250)
	nama_skretaris	=models.CharField(max_length = 1250)
	nama_anggota	=models.CharField(max_length = 25)
	deskripsi	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_organisasi)

class Model_skretaris(models.Model):
	nik	= models.CharField(max_length = 1200)
	nama	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 25)
	alamat	=models.CharField(max_length = 1250)
	nohp	=models.CharField(max_length = 25)
	foto	=models.ImageField(upload_to ='Berkas/', null=True)	
	jabatan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nik)

class Model_bendahara(models.Model):
	nik	= models.CharField(max_length = 1200)
	nama	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 25)
	alamat	=models.CharField(max_length = 1250)
	nohp	=models.CharField(max_length = 25)
	foto	=models.ImageField(upload_to ='Berkas/', null=True)	
	jabatan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nik)

# keuangan
class Model_keuangan(models.Model):
	nomor_keuangan	= models.CharField(max_length = 1200)
	nama_keuangan	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 25)
	keterangan	=models.CharField(max_length = 1250)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_keuangan)

# pengajuan proposal
class Model_proposal2(models.Model):
	jenis_proposal	= models.CharField(max_length = 1200)
	nama_anggota	=models.CharField(max_length = 1200)
	tema	=models.CharField(max_length = 25)
	tujuan_proposal	=models.CharField(max_length = 1250)
	upload_proposal	=models.FileField(max_length = 1250)
	status	=models.CharField(max_length = 1250)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis_proposal)
# proposal
class Model_syarat_proposal(models.Model):
	nama_proposal	= models.CharField(max_length = 1200)
	tema	=models.CharField(max_length = 1200)
	tujuan_proposal	=models.CharField(max_length = 1250)
	upload_proposal	=models.FileField(max_length = 1250)
	tanggal	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_proposal)

class Model_saran(models.Model):
	saran	= models.CharField(max_length = 1200)
	id_anggota	=models.CharField(max_length = 1200)
	nama_anggota	=models.CharField(max_length = 1250)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.saran)

class Model_pembina(models.Model):
	nik	= models.CharField(max_length = 1200)
	nama_pembina	=models.CharField(max_length = 1200)
	bidang	=models.CharField(max_length = 1250)
	nohp	=models.CharField(max_length = 1250)
	alamat	=models.CharField(max_length = 1250)
	jk	=models.CharField(max_length = 1250)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pembina)
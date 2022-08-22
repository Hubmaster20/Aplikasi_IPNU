from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_pimpinan, Model_surat_perintah, Model_anggota, Model_kegiatan, Model_organisasi1, Model_skretaris, Model_bendahara, Model_keuangan, Model_proposal2, Model_syarat_proposal, Model_saran, Model_pembina

admin.site.register(Model_pimpinan)
admin.site.register(Model_surat_perintah)
admin.site.register(Model_anggota)
admin.site.register(Model_kegiatan)
admin.site.register(Model_organisasi1)
admin.site.register(Model_skretaris)
admin.site.register(Model_bendahara)
admin.site.register(Model_keuangan)
admin.site.register(Model_proposal2)
admin.site.register(Model_syarat_proposal)
admin.site.register(Model_saran)
admin.site.register(Model_pembina)
from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    desa = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=20)
    kelahiran = models.DateField()
    pendidikan = models.CharField(max_length=50)
    nomor_sk = models.CharField(max_length=50)
    tanggal_sk = models.DateField()
    NIK = models.BigIntegerField()
    KK = models.BigIntegerField()
    hp = models.CharField(max_length=15, default='N/A')
    keterangan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
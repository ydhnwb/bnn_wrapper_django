from django.db import models

class Statistic(models.Model):
    total_kasus = models.CharField(max_length=255)
    total_tersangka = models.CharField(max_length=255)
    total_pasien_penyalahgunaan = models.CharField(max_length=255)
    jumlah_penggiat_anti_narkoba = models.CharField(max_length=255)
    jumlah_sebaran_informasi = models.CharField(max_length=255)

    def __str__(self):
        return "total kasus: {0}, total_tersangka: {1}, total pasien penyalahgunaan: {2}, " \
               "jumlah penggiat anti narkoba: {3}, jumlah sebaran informasi: {4}".format(
            self.total_kasus,self.total_tersangka, self.total_pasien_penyalahgunaan, self.jumlah_penggiat_anti_narkoba,
            self.jumlah_sebaran_informasi)

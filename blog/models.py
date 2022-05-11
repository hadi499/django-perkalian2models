
from django.utils import timezone
from django.db import models


class TarifPerKilo(models.Model):
    harga = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.harga


class Shipping(models.Model):
    nama = models.CharField(max_length=100)
    berat = models.IntegerField()

    def biaya_2(self):
        last = TarifPerKilo.objects.last()
        a = str(last)
        b = int(a)
        berat = self.berat
        return b * berat

    def __str__(self):
        return self.nama

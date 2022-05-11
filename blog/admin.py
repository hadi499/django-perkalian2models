from django.contrib import admin
from .models import Shipping, TarifPerKilo


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['nama', 'berat', 'biaya', 'create_at']


@admin.register(TarifPerKilo)
class TarifPerKiloAdmin(admin.ModelAdmin):
    list_display = ['harga', 'create_at']

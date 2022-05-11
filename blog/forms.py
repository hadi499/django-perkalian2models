from django import forms

from .models import Shipping, TarifPerKilo


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = [
            'nama',
            'berat',

        ]


class TarifPerKiloForm(forms.ModelForm):
    class Meta:
        model = TarifPerKilo
        fields = [
            'harga',
        ]

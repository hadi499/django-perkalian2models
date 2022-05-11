from django.shortcuts import render, redirect
from .forms import ShippingForm, TarifPerKiloForm
from blog.models import Shipping, TarifPerKilo


def home(request):
    shipping = Shipping.objects.all().order_by('-id')
    last = TarifPerKilo.objects.last()

    return render(request, 'blog/home.html', {'shipping': shipping, 'last': last})


def create(request):
    form = ShippingForm(request.POST)
    last = TarifPerKilo.objects.last()

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('home')

    context = {
        'form': form,
        'last': last
    }

    return render(request, 'blog/create.html', context)


def tarifperkilo(request):
    tarif = TarifPerKilo.objects.all().order_by('-id')

    return render(request, 'blog/tarif.html', {'tarif': tarif})


def ganti_tarif(request):
    form = TarifPerKiloForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('tarif')

    context = {
        'form': form,

    }

    return render(request, 'blog/ganti_tarif.html', context)

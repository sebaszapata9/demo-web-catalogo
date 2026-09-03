from django.shortcuts import render
from .models import Negocio, ProductoServicio



def lista_items(request):
  items = ProductoServicio.objects.all()
  return render(request,'catalogo.html', {'items': items})


def landing(request):
  data_negocio = Negocio.objects.first()
  return render(request, 'landing.html', {'data_negocio': data_negocio})


def detalle_item(request, slug):
  item = ProductoServicio.objects.get(slug=slug)
  return render(request, 'details.html', {'item': item})
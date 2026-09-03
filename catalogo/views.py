from django.shortcuts import render, get_object_or_404
from .models import Negocio, ProductoServicio



def lista_items(request):
  items = ProductoServicio.objects.all()
  return render(request,'catalogo.html', {'items': items})


def landing(request):
  data_negocio = Negocio.objects.first()
  return render(request, 'landing.html', {'data_negocio': data_negocio})


def detalle_item(request, slug):
  # Usamos get_object_or_404 para evitar errores si el slug no existe
  item = get_object_or_404(ProductoServicio, slug=slug)
  return render(request, 'item.html', {'item': item})
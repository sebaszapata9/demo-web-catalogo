from django.http import HttpResponse
from django.template import loader
from .models import ProductoServicio

def landing(request):
  template = loader.get_template('landing.html')
  return HttpResponse(template.render())

def producto_servicio(request):
  lista_productos = ProductoServicio.objects.all().values()
  template = loader.get_template('catalogo.html')
  context = {
    'productos': lista_productos,
  }
  return HttpResponse(template.render(context, request))
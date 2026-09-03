from django.contrib import admin
from .models import ProductoServicio, Negocio

# Register your models here.

class ProductoServicioAdmin(admin.ModelAdmin):
  list_display = ("nombre", "marca", "precio", "stock",)
  
admin.site.register(ProductoServicio, ProductoServicioAdmin)

class NegocioAdmin(admin.ModelAdmin):
  list_display = ("nombre", "direccion", "telefono", "correo_electronico")
  
admin.site.register(Negocio, NegocioAdmin)
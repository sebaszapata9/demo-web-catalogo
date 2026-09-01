from django.contrib import admin
from .models import ProductoServicio

# Register your models here.

class ProductoServicioAdmin(admin.ModelAdmin):
  list_display = ("nombre", "marca", "precio", "stock",)
  
admin.site.register(ProductoServicio, ProductoServicioAdmin)
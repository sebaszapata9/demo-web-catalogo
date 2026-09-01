from django.db import models

# Create your models here.
class ProductoServicio(models.Model):
	nombre = models.CharField(max_length=255)
	marca = models.CharField(max_length=255)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	slug = models.SlugField(unique=True)
	stock = models.PositiveIntegerField()
	ficha_tecnica = models.FileField(upload_to='fichas_tecnicas/', blank=True, null=True)
	stock_activo = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)


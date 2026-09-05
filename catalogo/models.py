from email.utils import quote

from django.db import models

# Create your models here.

class Negocio(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.TextField()
	direccion = models.CharField(max_length=255)
	telefono = models.CharField(max_length=20)
	correo_electronico = models.EmailField()
	logo = models.ImageField(upload_to='logos/', blank=True, null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)



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

	def __str__(self):
		return self.nombre

	def obtener_link_whatsapp(self):
		# Número de teléfono comercial de TodoTech SAC
		telefono = "51930741767"
		mensaje = (
			f"Hola, estoy interesado en el producto: {self.nombre}. ¿Me podrían dar"
			" más información?"
		)
		# quote se encarga de reemplazar espacios y caracteres especiales para URLs de forma segura
		mensaje_codificado = quote(mensaje)
		return f"https://wa.me/{telefono}?text={mensaje_codificado}"
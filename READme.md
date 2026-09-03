
READme de proyecto web catálogo
# READme



## paso a paso




### instalación inicial



1. creación de repositorio vacío en GitHub
2. clonación de repositorio en carpeta local
3. creación de virtual environment y activación del virtual env
4. ingreso a VSC y validación de que venv está activado
5. creación de proyecto en django: \[django-admin startproject demo\_web\_catalogo .]
6. validación de que se creó correctamente: \[python manage.py runserver]
7. creación de app catalogo: \[python manage.py startapp catalogo]
8. creación de archivo urls.py con configuración básica sin url patterns
9. inclusión de archivo catalogo.urls en archivo urls.py de proyecto principal (agregando el paquete include)
10. creación de carpeta templates dentro de app catalogo, y creación de archivo catalogo.html
11. HTML es la vista que debe ser renderizada en la función declarada dentro del archivo views.py. Creamos la función dentro del archivo catalogo/views.py
12. actualizar archivo settings, agregando la app creada 'catalogo'
13. Creación de modelo ProductoServicio en archivo models.py
14. Actualizar archivo catalogo/admin.py, agregando config set\_list display
15. instalar paquete Pillow: \[python -m pip install Pillow]
16. Correr las migraciones: \[python manage.py makemigrations catalogo]
17. Ejecutar las migraciones: \[python manage.py migrate]
18. Ejecutar comando de validación de migración ejecutada: \[python manage.py sqlmigrate catalogo 000X]
19. Creación de 5 ítems de catálogo ejemplo, ingresándolos en Python Shell: \[python manage.py shell] -> \[catalogo.models import ProductoServicio] -> \[ProductoServicio.objects.all()], más detalle en archivo en Notion sobre como cargar items: https://app.notion.com/p/Conceptos-b-sicos-3cb93cf60fb4802ab6ddfce3890d22d8



### realizando primera carga en git



1. \[git add --all]
2. \[git commit -m "Configuración inicial y carga de modelos"]
3. \[git push -u origin main]



### renderizando los datos del modelo



1. Crear un template en html básico para que veamos los productos renderizados, para saber más sobre esto ingresar al link en Notion: https://app.notion.com/p/Mostrar-data-3cb93cf60fb4801d8e4decfc9e6da599
2. declarar el modelo en el archivo views.py, creando una función que mostrará los ítems dentro del html
3. Hacer la conexión urls - views - templates/models
4. probar la conexión, creando un superuser para acceder al panel admin
5. testear 2 htmls, diseñados por gemini
6. validamos que los datos renderizan correctamente
7. disponibilizamos en el panel admin los modelos de productos e info del negocio


### Optimización de los htmls, carga de imagenes, y generación de links dinamicos por producto
1. Se optimizaron las páginas de landing y catalogo con colores de marca de la empresa ficticia
2. 
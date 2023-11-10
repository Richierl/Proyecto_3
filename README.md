# Artworks

El modelo básico de la aplicación es el siguiente:

```python
from django.db import models


class Artist(models.Model):
    slug = models.SlugField(max_length=80, unique=True)
    name = models.CharField(max_length=80)
    born_date = models.CharField(max_length=40)


class Genre(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Style(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Period(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Artwork(models.Model):
    author = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    path = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=40, null=True)
    style = models.ForeignKey(Style, null=True, on_delete=models.RESTRICT)
    period = models.ForeignKey(Period, null=True, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.RESTRICT)
    image_url = models.URLField()
```

Genera las tablas en PostgreSQL con `makemigrations` y `migrate`.
Una vez verifiacada la base de datos vamos a cargar algunos datos iniciales. Para cargar los datos sube a la instancia los datos del archivo `wikiart.zip` provisto.
Por ejemplo:

```
scp -i mi-llave-student.pem  wikiart.zip ubuntu@ittweb.ddns.net:/home/ubuntu
```
Instala el programa `unzip` y descomprime el archivo:
```
sudo apt install unzip
unzip wikiart.zip
rm -rf ___MACOSX
```
Antes de correr el script agrega una línea de conexión para la base de datos 
a tus variables de entorno. Por ejemplo:

```env
DB_DSN="dbname=artworks user=ubuntu password=MipasswordsupersecretO"
```
=======
# artworks

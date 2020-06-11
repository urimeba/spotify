import os
from django.conf import settings
from django.db import models
from Apps.User.models import User
from django.core.validators import FileExtensionValidator

def images_path(album, filename):
    return '{0}/{1}/{2}/{3}'.format("albums", album.artista, album.nombre, "cover.jpg")

def cancion_directory(instance, filename):
    numero_canciones = Cancion.objects.filter(album=instance.album).count()
    numero_canciones += 1

    return '{0}/{1}/{2}/{3}'.format("albums", instance.album.artista, instance.album, 
    str(numero_canciones) + " - " + instance.nombre + ".mp3" )


# Create your models here
class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DecimalField(max_digits=4, decimal_places=2)
    autor = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to=cancion_directory, null=False, blank=False, max_length=100,
    validators=[FileExtensionValidator(['mp3'])])
    
    def __str__(self):
        return "{} - {}".format(self.nombre, self.album)

    class Meta:
        verbose_name="Cancion"
        verbose_name_plural="Canciones"

class Album(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    foto = models.ImageField(upload_to=images_path, max_length=100, null=True, blank=True)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    disquera = models.ForeignKey('Disquera', on_delete=models.CASCADE)
    artista = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Disquera(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Playlist(models.Model):
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField()

    def __str__(self):
        return self.nombre

class PlaylistCanciones(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE)

    class Meta:
        verbose_name="PlaylistCanciones"
        verbose_name_plural="PlaylistsCanciones"

    def __str__(self):
        return self.pk

class UsuarioCanciones(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion', on_delete=models.CASCADE)

    class Meta:
        verbose_name="UsuarioCanciones"
        verbose_name_plural="UsuariosCanciones"

    def __str__(self):
        return self.pk


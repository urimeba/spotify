from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    return '/'.join(['fotos_perfil/', instance.username+'.jpg'])

# Create your models here.
class User(AbstractUser):
    PAISES = [
        ('MX', 'Mexico'),
        ('EU', 'Estados Unidos')
    ]

    is_premium = models.BooleanField(default=False, null=False, blank=False)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    pais = models.CharField(max_length=10, choices=PAISES, default='Mexico' , null=False, blank=False)
    foto = models.ImageField(upload_to=user_directory_path, height_field=None, width_field=None, max_length=100, blank=True, null=True)
    is_artist = models.BooleanField(default=False, null=False, blank=True)

    def isArtist(self):
        return self.is_artist

    


    
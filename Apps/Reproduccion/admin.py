from django.contrib import admin
from .models import Cancion, Album, Genero, Disquera, Playlist, PlaylistCanciones, UsuarioCanciones

# Register your models here.
admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Disquera)
admin.site.register(Playlist)
admin.site.register(PlaylistCanciones)
admin.site.register(UsuarioCanciones)
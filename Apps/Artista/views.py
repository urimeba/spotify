
from Apps.Reproduccion.models import Album, Cancion, Genero, Disquera
from django.shortcuts import render, HttpResponse
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def home(request):
    return render(request, 'home_artist.html')


@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def albums(request):
    todos_albums_artista = Album.objects.filter(artista=request.user).values('id')
    albums_con_canciones = Cancion.objects.filter(album__artista=request.user).values('album')
    albums_sin_canciones = todos_albums_artista.filter(~Q(id__in=albums_con_canciones))
    albums = Album.objects.filter(id__in=albums_sin_canciones)

    canciones = Cancion.objects.filter(album__artista=request.user)

    return render(request, 'albums_artista.html', {
        'canciones':canciones,
        'albums':albums
    })

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def perfil(request):
    return render(request, 'perfil_artista.html')

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def newAlbum(request):
    return render(request, 'new_album.html')

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def editAlbum(request, idAlbum):
    album = Album.objects.get(id=idAlbum)
    canciones = Cancion.objects.filter(album__id=idAlbum)
    return render(request, 'edit_album.html', {
        'canciones':canciones,
        'idAlbum':idAlbum,
        'album':album
    })

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def changePassword(request):
    return render(request, 'new_password.html')

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def actualizarAlbum(request):
    datos = json.loads(request.body)
    idAlbum = int(datos['idAlbum'])
    fechaAlbum = datos['fechaAlbum']
    generoAlbum = datos['generoAlbum']
    nombreAlbum = datos['nombreAlbum']

    try:
        album = Album.objects.get(id=idAlbum)
        album.fecha = fechaAlbum
        album.nombre = nombreAlbum

        genero_nuevo, fueCreado = Genero.objects.get_or_create(nombre=generoAlbum)
        album.genero = genero_nuevo
        album.save()
        return HttpResponse(True)

    except Exception as error:
        print(error)
        return HttpResponse(False)

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def eliminarAlbum(request):
    idAlbum = int(json.loads(request.body))
    print(idAlbum)

    try:
        album = Album.objects.get(id=idAlbum)
        album.delete()
        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(False)

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def agregarCancion(request):
    nombreCancion = request.POST['nombreCancion']
    duracionCancion = request.POST['duracionCancion']
    autorCancion = request.POST['autorCancion']
    idAlbum  = request.POST['idAlbum']
    archivoCancion = request.FILES['archivoCancion']

    try:
        Cancion.objects.create(
            nombre = nombreCancion,
            duracion = duracionCancion, 
            autor = autorCancion, 
            album_id = idAlbum,
            archivo = archivoCancion
        )
        print("TRY")
        return HttpResponse(True)
    except Exception as error:
        print(error)
        print("EXCEPT")
        return HttpResponse(False)

    return HttpResponse(False)

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def eliminarCancion(request):
    try:
        idCancion = request.POST['idCancion']
        cancion = Cancion.objects.get(id=idCancion)
        cancion.delete()
        return HttpResponse("Cancion eliminada correctamente")
    except Exception as error:
        print(error)
        return HttpResponse("Ha ocurrido un error al eliminar la cancion")

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def actualizarCancion(request):
    try:
        idCancion = request.POST['idCancion']
        cancion = Cancion.objects.get(id=idCancion)
        cancion.nombre = request.POST['nombreCancion']
        cancion.autor = request.POST['autorCancion']
        cancion.duracion = request.POST['duracionCancion']
        cancion.save()
        return HttpResponse("Cancion actualizada correctamente")
    except Exception as error:
        print(error)
        return HttpResponse("Ha ocurrido un error al actualizar la cancion")

@login_required
@user_passes_test(lambda user: user.isArtist()==True)
def agregarAlbum(request):
    try:
        nombreAlbum =  request.POST['nombreAlbum']
        fechaAlbum =  request.POST['fechaAlbum']
        disqueraAlbum =  request.POST['disqueraAlbum']
        generoAlbum =  request.POST['generoAlbum']
        numeroCanciones =  int(request.POST['numeroCanciones'])+1
        fotoAlbum =  request.FILES['fotoAlbum']

        canciones = []
        for x in range(0, numeroCanciones):
            numero = str(x)
            canciones.append(request.FILES['cancion['+numero+']'])

        genero, createdGenero = Genero.objects.get_or_create(nombre=generoAlbum)
        disquera, createdDisquera = Disquera.objects.get_or_create(nombre=disqueraAlbum)
        album_nuevo = Album.objects.create(
            nombre = nombreAlbum,
            fecha=fechaAlbum,
            foto=fotoAlbum,
            genero =genero,
            disquera=disquera,
            artista=request.user
        )

        for cancion in canciones:
            name = cancion.name
            name = name.split(".")[0]
            Cancion.objects.create(
                nombre = name,
                duracion = 1.00,
                autor = "Autor anonimo",
                album = album_nuevo,
                archivo = cancion
            )
         
        return HttpResponse(True)
    except Exception as error:
        print(error)
        return HttpResponse(False)


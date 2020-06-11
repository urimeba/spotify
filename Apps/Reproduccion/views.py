from django.shortcuts import render, HttpResponse
from .models import Cancion
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
        canciones = Cancion.objects.all()
        return render(request, 'home-rep.html', {
                'canciones': canciones
        })

@login_required
def busqueda(request):
        texto = request.POST['texto']
        if texto!="":
                canciones = Cancion.objects.filter(
                        Q(nombre__icontains=texto) |
                        Q(autor__icontains=texto) |
                        Q(album__nombre__icontains=texto) |
                        Q(album__genero__nombre__icontains=texto) |
                        Q(album__artista__username__icontains=texto)
                ).values_list('nombre', 'duracion', 'autor', 'album__nombre', 'archivo').order_by('album')

                lista = list(canciones)
                return JsonResponse({'lista': lista})
        else:
                canciones = Cancion.objects.all().values_list('nombre', 'duracion', 'autor', 'album__nombre', 'archivo').order_by('album')
                lista = list(canciones)
                return JsonResponse({'lista': lista})

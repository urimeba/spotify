"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Apps.Artista import views as views_artista

urlpatterns = [
    path('', views_artista.home, name='home_artista'),
    path('albums/', views_artista.albums, name='albums'),
    path('perfil/', views_artista.perfil, name='perfil'),
    path('new_password/', views_artista.changePassword, name='changePassword'),
    path('albums/new', views_artista.newAlbum, name='newAlbum'),
    path('albums/edit/<int:idAlbum>', views_artista.editAlbum, name='editAlbum'),
    path('albums/update', views_artista.actualizarAlbum, name='actualizarAlbum'),
    path('albums/delete', views_artista.eliminarAlbum, name='eliminarAlbum'),
    path('albums/add', views_artista.agregarAlbum, name='agregarAlbum'),
    

    path('cancion/add', views_artista.agregarCancion, name='agregarCancion'),
    path('cancion/delete', views_artista.eliminarCancion, name='eliminarCancion'),
    path('cancion/update', views_artista.actualizarCancion, name='actualizarCancion'),
    

]

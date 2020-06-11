from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from Apps.Reproduccion import views as views_reproduccion
from Apps.Artista import views as views_artista
from Apps.Reproduccion import views as views_reproduccion
from Apps.User.models import User
from django.contrib.auth.decorators import login_required

def home(request): 
    if(request.user.is_authenticated):
        if(request.user.is_artist):
            return redirect('home_artista')
        else:
            return redirect('home-reproduccion')
    else:
        return render(request, 'home.html')

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if(user.is_artist):
                    return redirect(views_artista.home)
                else:
                    return redirect(views_reproduccion.home)
            else:
                form.add_error(None, 'Revisa tus datos')
                return render(request, 'login.html', {'form':form})
        else:
            return HttpResponse('Revisa tu formulario')

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def register(request):
    
    
    if request.method=='POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password'] 
            email = form.cleaned_data['email'] 
            nombre = form.cleaned_data['first_name'] 
            apellido =form.cleaned_data['last_name'] 
            fechaNacimiento =form.cleaned_data['fechaNacimiento'] 
            pais =form.cleaned_data['pais'] 
            foto = form.cleaned_data.get('foto')
            is_artist = form.cleaned_data['is_artist'] 

            user = User.objects.filter(username=username)
            email_user = User.objects.filter(email=email)

            if(len(user)>0):
                form.add_error('username', 'Este nombre de usuario ya esta registrado')
                return render(request, 'register.html', {'form':form})

            if(len(email_user)>0):
                form.add_error('email', 'Este correo ya esta registrado')
                return render(request, 'register.html', {'form':form})

            user = User(
                username = username,
                email = email,
                first_name = nombre,
                last_name = apellido,
                fechaNacimiento = fechaNacimiento,
                pais = pais,
                foto = foto,
                is_artist = is_artist,
            )
            user.set_password(password)
            user.save()
            form.add_error(None, 'Usuario creado exitosamente')
            return render(request, 'register.html', {'form':form})

        else:
            return render(request, 'register.html', {'form':form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect(home)
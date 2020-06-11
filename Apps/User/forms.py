from django import forms
from django.forms import ModelForm, Textarea
# from django.contrib.auth.models import User
from Apps.User.models import User
import datetime


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Ingresa tu usuario', min_length=5, required=True, widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario', 'class':'form-control'}))
    password = forms.CharField(max_length=50, label='Ingresa tu contraseña' , min_length=5, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email','first_name', 'last_name', 'pais', 'fechaNacimiento', 'foto', 'is_artist' ]
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'correo@correo.com'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'required':'True', 'placeholder':'Nombre(s)'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'required':'True', 'placeholder':'Apellido(s)'}),

            'pais':forms.Select(attrs={'class':'form-control', 'required':'true', 'placeholder':'Ingresa tu fecha de nacimiento'}),
            'fechaNacimiento':forms.DateInput(format='%d/%m/%Y',attrs={'class':'form-control', 'placeholder':'DD/MM/AAAA'}),
            'foto':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Hola'}),
            'is_artist':forms.CheckboxInput(attrs={'class':'form-check-label'}),

        }

        labels={
            'fechaNacimiento':'Fecha de Nacimiento',
            'pais':'Pais actual'  ,
            'foto':'Foto de perfil',
        }

        help_texts={
            'username': 'Maximo 150 caracteres',
            'password': 'Minimo 8 caracteres',
            'foto':'Foto de perfil (Opcional)',
            'fechaNacimiento':'Fecha de Nacimiento (Opcional)',
            'pais':'País actual donde radicas (Obligatorio)',
            'email':'Obligatorio',
            'first_name':'Obligatorio',
            'last_name':'Obligatorio',
        }
       

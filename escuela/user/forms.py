from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import defaultUser as User
from .models import Area
from django.db import models
from django.contrib.auth.models import User as Us

class UsuarioModelForm(UserCreationForm):
    opciones = {
        'M':'M',
        'F':'F'
    }
    
    username = forms.CharField(label=('Usuario'))
    first_name = forms.CharField(label=('Nombre'))
    last_name = forms.CharField(label=('Apellido'))
    sexo = forms.ChoiceField(label=('Sexo'),choices=opciones)
    password1 = forms.CharField(
        label=('Contraseña'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=('Confirmar contraseña'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    
    Área = models.ForeignKey(Area,on_delete=models.CASCADE)
    
    class Meta:
      model = User
      fields = ('username','first_name','last_name', 'sexo','password1', 'password2','Área')
    
    
    
class UsuarioUpdateModelForm(forms.ModelForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    Área = models.ForeignKey( Area ,on_delete=models.CASCADE)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'Área')
    

class login(UserCreationForm):
    password1 = forms.CharField(
        label=('Contraseña')
      )
    class Meta:
      model = Us
      fields = ['username','password']
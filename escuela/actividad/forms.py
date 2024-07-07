from django import forms
from .models import actividad
from django.forms import ValidationError
from django.core.validators import RegexValidator

class modificar(forms.ModelForm):
            
    class Meta:
        model= actividad
        fields = ['Nombre','Autor','Clasificacion']


class registrar(forms.ModelForm):


    class Meta:
        model = actividad
        fields = '__all__'
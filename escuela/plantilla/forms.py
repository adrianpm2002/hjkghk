from django import forms
from .models import plantilla
from user.models import User

class modificar(forms.ModelForm):
    Trabajadores = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'usuarios-selector'}),
        required=False
    )
    class Meta:
        model= plantilla
        fields = ['Nombre','Autor','Trabajadores']

class registrar(forms.ModelForm):
    Trabajadores = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'usuarios-selector'}),
        required=False
    )
    class Meta:
        model= plantilla
        fields = ['Nombre','Autor','Trabajadores','Fecha']
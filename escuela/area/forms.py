from django import forms
from .models import area1

class modificar(forms.ModelForm):

    class Meta:
        model= area1
        fields = ['Nombre_del_area','Encargado','Cantidad_de_personal','Plantilla']
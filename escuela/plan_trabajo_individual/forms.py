from django import forms
from .models import plan_trabajo_individual

class clasificar(forms.ModelForm):

    class Meta:
        model = plan_trabajo_individual
        fields = ['clasification']

class modificar(forms.ModelForm):

    class Meta:
        model= plan_trabajo_individual
        fields = ['Titulo','Autor','Nivel_jerarquico','actividades_generales','actividad_principal']
from django import forms
from .models import plan_trabajo

class modificar(forms.ModelForm):

    class Meta:
        model= plan_trabajo
        fields = ['Titulo','Autor','Nivel_jerarquico','actividades_generales','actividades_principales']
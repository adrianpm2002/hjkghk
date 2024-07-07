from django import forms
from .models import informe_cumplimiento
from django.core.validators import RegexValidator

class modificar(forms.ModelForm):
    Titulo = forms.CharField(min_length=3,max_length=30) 
    Total_tareas_planificadas= forms.IntegerField(min_value=0, max_value=30)
    Cumplidas= forms.IntegerField(min_value=0, max_value=30)
    Incumplidas= forms.IntegerField(min_value=0, max_value=30)
    Nuevas_incorporadas= forms.IntegerField(min_value=0, max_value=30)
    Modificadas = forms.IntegerField(min_value=0, max_value=30)
    class Meta:
        model= informe_cumplimiento
        fields = ['Titulo','Autor','Total_tareas_planificadas','Cumplidas','Incumplidas','Nuevas_incorporadas','Modificadas','Descripcion']

class registrar(forms.ModelForm):
    Titulo = forms.CharField(label="Título",min_length=3,max_length=30) 
    Total_tareas_planificadas= forms.IntegerField(min_value=0, max_value=30)
    Cumplidas= forms.IntegerField(min_value=0, max_value=30)
    Incumplidas= forms.IntegerField(min_value=0, max_value=30)
    Nuevas_incorporadas= forms.IntegerField(min_value=0, max_value=30)
    Modificadas = forms.IntegerField(min_value=0, max_value=30)
    class Meta:
        model= informe_cumplimiento
        fields = ['Titulo','Autor','Fecha','Total_tareas_planificadas','Cumplidas','Incumplidas','Nuevas_incorporadas','Modificadas','Descripcion']   
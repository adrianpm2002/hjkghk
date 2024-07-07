from django.db import models
from datetime import date
from user.models import User
from actividad.models import actividad
# Create your models here...

class plan_trabajo_individual(models.Model):
    clas = {
        'Decano':'Decano',
        'Vice Decano':'Vice Decano',
        'Rector':'Rector',
        'Jefe de departamento':'Jefe de departamento',
        'Profesor':'Profesor',
    }

    calificacion={
        'Aprobado':'Aprobado',
        'No aprobado':'No aprobado'
    }
    Titulo = models.CharField('Título',max_length=200)
    Autor = models.ForeignKey(User,on_delete=models.CASCADE)
    Nivel_jerarquico= models.CharField('Nivel Gerárquico',max_length=100, choices= clas)
    Fecha_inicio = models.DateField(default= date.today)
    Fecha_fin = models.DateField()
    actividades_generales = models.ManyToManyField(actividad, related_name='actividades_generales_pti', limit_choices_to={'Clasificacion': 'General'})
    actividad_principal = models.ManyToManyField(actividad, related_name='actividad_principal_pti', limit_choices_to={'Clasificacion': 'Principal'})
    clasification = models.CharField('Clasificación',max_length= 30, choices = calificacion)
    def __str__(self):
        return self.Titulo


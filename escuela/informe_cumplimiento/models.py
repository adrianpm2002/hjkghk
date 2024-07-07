from django.db import models
from datetime import date
from user.models import User
# Create your models here..
class informe_cumplimiento(models.Model):
    Titulo = models.CharField('Título',max_length=200)
    Autor = models.ForeignKey(User,on_delete=models.CASCADE)
    Fecha = models.DateField(default= date.today)
    Total_tareas_planificadas=models.IntegerField()
    Cumplidas = models.IntegerField()
    Incumplidas = models.IntegerField()
    Nuevas_incorporadas= models.IntegerField()
    Modificadas = models.IntegerField()
    Descripcion = models.TextField("Descripción",max_length=1000)
    def __str__(self):
        return self.Titulo
    

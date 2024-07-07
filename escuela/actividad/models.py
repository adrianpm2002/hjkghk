from django.db import models
from datetime import date
from user.models import User
from django.core.validators import RegexValidator

# Create your models here..
class actividad(models.Model):
    clasificaciones = {
        'General':'General',
        'Principal':'Principal'
    }

  
    Nombre = models.CharField(max_length=50)
    Autor = models.ForeignKey(User,on_delete=models.CASCADE)
    Clasificacion = models.CharField('Clasificación',max_length=100, choices= clasificaciones)
    Fecha = models.DateField(default= date.today)
    def __str__(self):
        return self.Nombre
    
    
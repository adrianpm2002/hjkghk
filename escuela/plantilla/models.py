from django.db import models
from datetime import date
from user.models import User
from multiselectfield import MultiSelectField
# Create your models here..
class plantilla(models.Model):
    
    Nombre = models.CharField(max_length=200)
    Autor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='autor')
    Trabajadores = models.ManyToManyField(User, related_name='trabajador')
    Fecha = models.DateField(default= date.today)
    def __str__(self):
        return self.Nombre
    

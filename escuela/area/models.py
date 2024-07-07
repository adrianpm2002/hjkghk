from django.db import models
from datetime import date
from user.models import User
from plantilla.models import plantilla
# Create your models here..
class area1(models.Model):
    clasificaciones = {
        'General':'General',
        'Principal':'Principal'
    }
    Nombre_del_area = models.CharField('Nombre',max_length=200)
    Encargado = models.ForeignKey(User,on_delete=models.CASCADE)
    Cantidad_de_personal = models.IntegerField()
    Fecha = models.DateField(default= date.today)
    Plantilla = models.ForeignKey(plantilla,on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre_del_area
    

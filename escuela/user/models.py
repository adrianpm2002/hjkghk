from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Area(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)
    cantidad_profesores = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.nombre

    
class defaultUser(User):
    opciones = {
        'M':'M',
        'F':'F'
    }
    clas = {
        'Decano':'Decano',
        'Vice Decano':'Vice Decano',
        'Rector':'Rector',
        'Jefe de departamento':'Jefe de departamento',
        'Profesor':'Profesor',
    }
    Área = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)
    sexo = models.CharField('Sexo',max_length = 1, choices = opciones, default = "M")
    Rol_de_usuario = models.CharField('Rol de usuario',max_length= 30, choices = clas, null=True,default="Profesor")
    def __str__(self) -> str:
        return self.username
    
    
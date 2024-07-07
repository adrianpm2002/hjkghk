from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import listUser,modificarRol,asignarRol

urlpatterns = [
    path('list_user/',listUser.as_view(),name= 'listar_usuario_rol'),
    path('update_rol/<int:pk>',modificarRol.as_view(),name = 'updateRol'),
    path('asignar_rol/',asignarRol.as_view(),name = 'asignarRol'),
]
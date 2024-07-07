from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updateActividad,createActividad,listActividad,deleteActividad,autocomplete

urlpatterns = [
    path('act_update/<int:pk>',updateActividad.as_view(),name='update_actividad'),
    path('act_create/',createActividad.as_view(),name ='create_actividad'),
    path('act_list/',listActividad.as_view(),name = 'list_actividad'),
    path('act_delete/<int:pk>',deleteActividad.as_view(), name= 'delete_actividad'),
    #path('base/',perfilUsuario.as_view(),name = 'base'),
    path('autocomplete/', autocomplete, name='autocomplete'),
] 
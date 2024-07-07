from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updatePlantilla,createPlantilla,listPlantilla,deletePlantilla

urlpatterns = [
    path('pll_update/<int:pk>',updatePlantilla.as_view(),name='update_pll'),
    path('pll_create/',createPlantilla.as_view(),name ='create_pll'),
    path('pll_list/',listPlantilla.as_view(),name = 'list_pll'),
    path('pll_delete/<int:pk>',deletePlantilla.as_view(), name= 'delete_pll')
] 
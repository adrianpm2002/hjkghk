from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updateArea,createArea,listArea,deleteArea

urlpatterns = [
    path('area_update/<int:pk>',updateArea.as_view(),name='update_area'),
    path('area_create/',createArea.as_view(),name ='create_area'),
    path('area_list/',listArea.as_view(),name = 'list_area'),
    path('area_delete/<int:pk>',deleteArea.as_view(), name= 'delete_area')
] 
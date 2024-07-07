from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updateActividad,createActividad,listActividad,deleteActividad,DashboardView

urlpatterns = [
    path('ic_update/<int:pk>',updateActividad.as_view(),name='update_ic'),
    path('ic_create/',createActividad.as_view(),name ='create_ic'),
    path('ic_list/',listActividad.as_view(),name = 'list_ic'),
    path('ic_delete/<int:pk>',deleteActividad.as_view(), name= 'delete_ic'),
    path('grafico/',DashboardView.as_view(),name = 'grafico'),
] 
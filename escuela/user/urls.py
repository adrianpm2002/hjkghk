from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import UserLoginView,listUserView, salir,UserCreateView, userUpdateview, userDeleteView


urlpatterns = [
    path('',UserLoginView.as_view(), name='login'),
    path('users/',listUserView.as_view(), name = 'listUser'),
    path('createuser/', UserCreateView.as_view(), name = 'crearuser'),
    path('editaruser/<int:pk>',userUpdateview.as_view() ,name = 'editaruser'),
    path('eliminaruser/<int:pk>',userDeleteView.as_view() ,name = 'eliminaruser'),
    path('salir/',salir,name="salir")
       
]
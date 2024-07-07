"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('act/',include('actividad.urls')),
    path('home/',home.as_view(),name='index'),
    path('pt/',include('plan_trabajo.urls')),
    path('ic/',include('informe_cumplimiento.urls')),
    path('area/',include('area.urls')),
    path('pll/',include('plantilla.urls')),
    path('pti/',include('plan_trabajo_individual.urls')),
    path('admin_rol_user/',include('administrar_roles_usuario.urls')),
    #path('base/',perfilUsuario.as_view(),name = 'base'),
    
    
]

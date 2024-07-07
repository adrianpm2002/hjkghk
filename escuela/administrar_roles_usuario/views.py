
from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView
from user.models import defaultUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from typing import Any
#from .forms import modificar
# Create your views here.

class listUser(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = defaultUser
    template_name = 'userLi.html' 
    context_object_name = 'users'  
    paginate_by = 10
    
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return User.objects.filter(username__icontains=q)
        
        return super().get_queryset()

class modificarRol(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = defaultUser
    template_name = 'modificarRol.html'
    success_url = reverse_lazy('listar_usuario_rol')
    #form_class = modificar
    fields = ['Rol_de_usuario']

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Asignación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class asignarRol(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = defaultUser
    template_name = 'asignarRol.html'
    success_url = reverse_lazy('listar_usuario_rol')
    #form_class = modificar
    fields = ['Rol_de_usuario']

    
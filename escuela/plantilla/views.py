from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import plantilla
from django.urls import reverse_lazy
from .forms import modificar,registrar
from django.db.models import Q
from user.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from typing import Any



# Create your views here...
class updatePlantilla(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plantilla
    form_class= modificar
    template_name = 'update_pll.html'
    success_url = reverse_lazy('list_pll')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class createPlantilla(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plantilla
    template_name = 'registrar_pll.html'
    form_class = registrar
    success_url = reverse_lazy('list_pll')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

    

class listPlantilla(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = plantilla
    template_name = 'listar_pll.html'
    context_object_name = 'pll' 
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return plantilla.objects.filter(Nombre__icontains=q)
        
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context

class deletePlantilla(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = plantilla
    template_name = 'eliminar_pll.html'
    success_url = reverse_lazy('list_pll') 

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = self.get_object()
        self.object.delete()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    
    

    
    

    

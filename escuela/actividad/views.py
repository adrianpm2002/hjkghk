from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView
from .models import actividad
from django.urls import reverse_lazy,reverse
from .forms import modificar,registrar
from django.db.models import Q
from user.models import User,defaultUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.db.models import Q
from django.forms import ValidationError
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from typing import Any




# Create your views here...
class updateActividad(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = actividad
    form_class = modificar
    template_name = 'update_actividad.html'
    success_url = reverse_lazy('list_actividad')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class createActividad(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = actividad
    template_name = 'registrar_actividad.html'
    form_class = registrar
    def get_success_url(self):
        return reverse_lazy('list_actividad')
    
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class listActividad(ListView,LoginRequiredMixin):
    model = actividad
    
    template_name = 'Actividades.html'
    
    context_object_name = 'act' 

    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return actividad.objects.filter(Nombre__icontains=q)
        
        return super().get_queryset()
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context
    
class deleteActividad(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = actividad
    template_name = 'eliminar_actividad.html'
    success_url = reverse_lazy('list_actividad') 
    
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = self.get_object()
        self.object.delete()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

def autocomplete(request):
    if 'term' in request.GET:
        qs = actividad.objects.filter(
            Q(Nombre__icontains=request.GET.get('term')) |
            Q(Autor__icontains=request.GET.get('term'))
        )
        act = list(qs.values('id', 'Nombre'))
        return JsonResponse(act, safe=False)
    return JsonResponse({})
    

    
    

    

from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView
from .models import informe_cumplimiento
from django.urls import reverse_lazy
from .forms import modificar,registrar
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from typing import Any
from django.db.models import Sum





# Create your views here...
class updateActividad(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = informe_cumplimiento
    form_class= modificar
    template_name = 'update_ic.html'
    success_url = reverse_lazy('list_ic')
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class createActividad(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = informe_cumplimiento
    template_name = 'registrar_ic.html'
    form_class = registrar
    success_url = reverse_lazy('list_ic')
    
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class listActividad(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = informe_cumplimiento
    template_name = 'listar_ic.html'
    context_object_name = 'ic' 
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return informe_cumplimiento.objects.filter(Titulo__icontains=q)
        
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
    model = informe_cumplimiento
    template_name = 'eliminar_ic.html'
    success_url = reverse_lazy('list_ic') 

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = self.get_object()
        self.object.delete()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    
class DashboardView(TemplateView):
    model = informe_cumplimiento
    template_name = "grafico_ic.html"

    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)

        # Calcula las sumas para cada campo
        total_tareas_planificadas = informe_cumplimiento.objects.aggregate(
            total=Sum('Total_tareas_planificadas')
        )['total']
        total_cumplidas = informe_cumplimiento.objects.aggregate(
            total=Sum('Cumplidas')
        )['total']
        total_modificadas = informe_cumplimiento.objects.aggregate(
            total=Sum('Modificadas')
        )['total']
        total_agregadas = informe_cumplimiento.objects.aggregate(
            total=Sum('Nuevas_incorporadas')
        )['total']
        total_incumplidas = informe_cumplimiento.objects.aggregate(
            total=Sum('Incumplidas')
        )['total']

        # Agrega las variables al contexto
        context['total_tareas_planificadas'] = total_tareas_planificadas
        context['total_cumplidas'] = total_cumplidas
        context['total_modificadas'] = total_modificadas
        context['total_agregadas'] = total_agregadas
        context['total_incumplidas'] = total_incumplidas

        return context
    
    

    
    

    

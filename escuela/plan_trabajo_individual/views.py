from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import plan_trabajo_individual
from django.urls import reverse_lazy
from .forms import modificar,clasificar
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from typing import Any
from reportlab.pdfgen import canvas
from django.http import HttpResponse



# Create your views here...
class updatePlanTrabajoIndividual(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo_individual
    form_class= modificar
    template_name = 'update_pti.html'
    success_url = reverse_lazy('list_pti')
    

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class createPlanTrabajoIndividual(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo_individual
    template_name = 'registrar_pti.html'
    fields = ['Titulo','Autor','Nivel_jerarquico','Fecha_inicio','Fecha_fin','actividades_generales','actividad_principal']
    success_url = reverse_lazy('list_pti')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class listPlanTrabajoIndividual(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo_individual
    template_name = 'listar_pti.html'
    context_object_name = 'plan_t_i' 
    image_url = 'escuela/static/todo/img/arbol-de-decision.png'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return plan_trabajo_individual.objects.filter(Titulo__icontains=q)
        
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context

class deletePlanTrabajoIndividual(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo_individual
    template_name = 'eliminar_pti.html'
    success_url = reverse_lazy('list_pti') 

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = self.get_object()
        self.object.delete()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class clasificarPlanTrabajoIndividual(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo_individual
    form_class= clasificar
    template_name = 'clasificar.html'
    success_url = reverse_lazy('list_pti')
    
    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Clasificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

    
    
def exportar_a_pdf(request, Titulo=None):
    if not Titulo:
        Titulo = request.GET.get('Titulo')
    
    if not Titulo:
        return HttpResponse("Título no proporcionado", status=400)
    
    try:
        plan = plan_trabajo_individual.objects.get(Titulo=Titulo)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{plan.Titulo}.pdf"'

        # Crear el documento PDF usando reportlab
        pdf = canvas.Canvas(response)
        pdf.drawString(100, 750, f"Información de {plan.Titulo}:")
        pdf.drawString(100, 730, f"Titulo: {plan.Titulo}")
        pdf.drawString(100, 710, f"Autor: {plan.Autor}")
        pdf.drawString(100, 690, f"Nivel Jerarquico: {plan.Nivel_jerarquico}")
        pdf.drawString(100, 670, f"Fecha Inicio: {plan.Fecha_inicio}")
        pdf.drawString(100, 650, f"Fecha Fin: {plan.Fecha_fin}")
        pdf.drawString(100, 630, f"Actividades Generales: {plan.actividades_generales}")
        pdf.drawString(100, 610, f"Actividad Principal: {plan.actividad_principal}")
        pdf.drawString(100, 590, f"Calificación: {plan.clasification}")
        pdf.showPage()
        pdf.save()

        return response
    except plan_trabajo_individual.DoesNotExist:
        return HttpResponse("Plan no encontrado", status=404)

    

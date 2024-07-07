from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import plan_trabajo
from django.urls import reverse_lazy
from .forms import modificar
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from typing import Any
from reportlab.pdfgen import canvas
from django.http import HttpResponse




# Create your views here...
class updatePlanTrabajo(UpdateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo
    form_class= modificar
    template_name = 'update_PT.html'
    success_url = reverse_lazy('list_pt')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Modificación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class createPlanTrabajo(CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo
    template_name = 'registrar_PT.html'
    fields = '__all__'
    success_url = reverse_lazy('list_pt')

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = form.save()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Registro satisfactorio')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())

class listPlanTrabajo(ListView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo
    template_name = 'listar_PT.html'
    context_object_name = 'plan_t' 
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return plan_trabajo.objects.filter(Titulo__icontains=q)
        
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'defaultuser'):
            context['user'] = user.defaultuser
        else:
            context['user'] = user
        return context
    
class deletePlanTrabajo(DeleteView,LoginRequiredMixin, UserPassesTestMixin):
    model = plan_trabajo
    template_name = 'eliminar_PT.html'
    success_url = reverse_lazy('list_pt') 

    def form_valid(self, form):
        # Resto del código de la vista
        self.object = self.get_object()
        self.object.delete()
        # Agregar mensaje de éxito
        messages.success(self.request, 'Eliminación satisfactoria')

        # Redirigir al usuario a la URL de éxito
        return redirect(self.get_success_url())
    


def exportar_a_pdfPT(request, Titulo=None):
    if not Titulo:
        Titulo = request.GET.get('Titulo')
    
    if not Titulo:
        return HttpResponse("Título no proporcionado", status=400)
    
    try:
        plan = plan_trabajo.objects.get(Titulo=Titulo)

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
        pdf.drawString(100, 610, f"Actividad Principal: {plan.actividades_principales}")
        

        pdf.showPage()
        pdf.save()

        return response
    except plan_trabajo.DoesNotExist:
        return HttpResponse("Plan no encontrado", status=404)
    

    
    

    

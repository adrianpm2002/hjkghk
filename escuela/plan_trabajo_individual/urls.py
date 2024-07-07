from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updatePlanTrabajoIndividual,createPlanTrabajoIndividual,listPlanTrabajoIndividual,clasificarPlanTrabajoIndividual,deletePlanTrabajoIndividual,exportar_a_pdf

urlpatterns = [
    path('pti_update/<int:pk>',updatePlanTrabajoIndividual.as_view(),name='update_pti'),
    path('pti_create/',createPlanTrabajoIndividual.as_view(),name ='create_pti'),
    path('pti_list/',listPlanTrabajoIndividual.as_view(),name = 'list_pti'),
    path('pti_delete/<int:pk>',deletePlanTrabajoIndividual.as_view(), name= 'delete_pti'),
    path('clas_pti/<int:pk>',clasificarPlanTrabajoIndividual.as_view(),name = 'clasificar'),
    path('exportar/', exportar_a_pdf, name='exportar_a_pdf'),
    path('exportar/<str:Titulo>/',exportar_a_pdf, name='exportar_a_pdf_con_titulo'),
] 
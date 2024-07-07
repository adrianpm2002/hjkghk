from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import updatePlanTrabajo,createPlanTrabajo,listPlanTrabajo,deletePlanTrabajo,exportar_a_pdfPT

urlpatterns = [
    path('pt_update/<int:pk>',updatePlanTrabajo.as_view(),name='update_pt'),
    path('pt_create/',createPlanTrabajo.as_view(),name ='create_pt'),
    path('pt_list/',listPlanTrabajo.as_view(),name = 'list_pt'),
    path('pt_delete/<int:pk>',deletePlanTrabajo.as_view(), name= 'delete_pt'),
    path('exportar/', exportar_a_pdfPT, name='exportar_a_pdfPT'),
    path('exportar/<str:Titulo>/',exportar_a_pdfPT, name='exportar_a_pdf_con_tituloPT'),
] 
from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/filtro/', views.filtrar_alunos, name='relatorioslist'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.filtrar_alunos, name='relatorioslist'),
    path('relatorios/defesa/', views.relatorio_defesa, name='relatorio_defesa'),
    path('alunos/filtrar/', views.filtrar_alunos, name='filtrar_alunos')
]
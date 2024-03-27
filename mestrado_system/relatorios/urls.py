from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.relatorioslist, name='relatorioslist'),
    path('relatorios/defesa/', views.relatorio_defesa, name='relatorio_defesa'),
]
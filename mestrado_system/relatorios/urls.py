from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.relatorioslist, name='relatorioslist'),
    path('buscar/', views.buscar_produto, name='buscar_produto'),   
]
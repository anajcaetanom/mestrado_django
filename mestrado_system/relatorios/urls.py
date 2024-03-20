from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.relatorioslist, name='relatorioslist'),
]
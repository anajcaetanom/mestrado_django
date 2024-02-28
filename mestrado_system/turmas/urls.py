from django.urls import path
from . import views

urlpatterns = [
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/details/<int:id>/', views.details, name='details'),
    path('editar-turma/<int:turma_id>/', views.editar_turma, name='editar_turma'),
    path('criar-turma/', views.criar_turma, name='criar_turma'),
    path('excluir-turmas/<int:turma_id>/', views.excluir_turma, name='excluir_turma'),
    path('', views.main, name='main'),
]

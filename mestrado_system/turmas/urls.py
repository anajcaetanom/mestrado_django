from django.urls import path
from . import views

urlpatterns = [
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/details/<int:id>/', views.details, name='details'),
    path('editar_turma/<int:turma_id>/', views.editar_turma, name='editar_turma'),
    path('criar_turma/', views.criar_turma, name='criar_turma'),
    path('excluir_turmas/<int:turma_id>/', views.excluir_turma, name='excluir_turma'),
    path('alunos_da_turma/<int:id>/', views.alunos_da_turma, name='alunos_da_turma'),
    path('', views.main, name='main'),
]

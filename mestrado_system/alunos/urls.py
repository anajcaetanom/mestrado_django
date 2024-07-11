from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('criar-aluno/', views.criar_aluno, name='criar_aluno'),
    path('editar-aluno/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir-aluno/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
    path('<str:prefix>/alunoInfo/<int:id>/', views.alunoInfo, name='alunoInfo'),
]
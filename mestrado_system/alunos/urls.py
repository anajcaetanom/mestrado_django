from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/alunoInfo/<int:id>/', views.alunoInfo, name='alunoInfo'),
    path('criar_aluno/', views.criar_aluno, name='criar_aluno'),
    path('editar_aluno/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('alunos-desistencia/', views.alunos_desistencia, name='alunos_desistencia'),
    path('alunos/alunoInfo/<int:id>/', views.alunoInfo, name='alunoInfo'),
    path('criar-aluno/', views.criar_aluno, name='criar_aluno'),
    path('editar-aluno/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir-aluno/<int:aluno_id>/', views.excluir_aluno, name='excluir_aluno'),
    path('filtrar/', views.filtrar_alunos, name='filtrar_alunos'),
    path('desistencia/<int:aluno_id>/', views.desistencia, name='desistencia'),
    path('jubilado/<int:aluno_id>/', views.jubilado, name='jubilado'),
    path('trancamento/<int:aluno_id>/', views.trancamento, name='trancamento'),
]
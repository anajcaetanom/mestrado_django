from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/alunoInfo/<int:id>/', views.alunoInfo, name='alunoInfo'),
    path('criar_aluno/', views.criar_aluno, name='criar_aluno'),
]
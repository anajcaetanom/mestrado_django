from django.urls import path
from . import views

urlpatterns = [
    path('alunos/', views.alunos, name='alunos'),
    path('aluno/alunoInfo/<int:id>', views.alunoInfo, name='alunoInfo'),
]
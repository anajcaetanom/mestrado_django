from django.urls import path
from . import views

urlpatterns = [
    path('docentes/', views.docentes, name='docentes'),
    path('docentes/docenteInfo/<int:id>/', views.docenteInfo, name='docenteInfo'),
    path('criar-docente/', views.criar_docente, name='criar_docente'),
    path('editar-docente/<int:docente_id>/', views.editar_docente, name='editar_docente'),
    path('excluir-docente/<int:docente_id>/', views.excluir_docente, name='excluir_docente'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('turmas/', views.turmas, name='turmas'),
    path('turmas/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
]

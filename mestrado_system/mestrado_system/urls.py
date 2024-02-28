from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('' , include('turmas.urls')),
    path('' , include('alunos.urls')),
    path('' , include('users.urls')),
    path('admin/', admin.site.urls),
]

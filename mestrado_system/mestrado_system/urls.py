from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('turmas.urls')),
    path('' , include('alunos.urls')),
    path('' , include('users.urls')),
    path('' , include('docentes.urls')),
    path('' , include('relatorios.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

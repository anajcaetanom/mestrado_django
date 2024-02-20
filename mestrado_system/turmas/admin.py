from django.contrib import admin
from .models import Turma

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_de_criacao",)

admin.site.register(Turma, TurmaAdmin)

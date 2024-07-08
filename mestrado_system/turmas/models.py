from django.db import models
from django.utils import timezone

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    vagas = models.IntegerField(null=True)
    curso = models.CharField(max_length=255)
    data_de_inicio = models.DateField(null=True)
    data_de_criacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome

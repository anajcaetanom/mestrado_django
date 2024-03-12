from django.db import models
from alunos.models import Aluno

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    orientados = models.ManyToManyField(Aluno, related_name='docentes_orientadores', blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

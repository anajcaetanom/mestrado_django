from django.db import models
from turmas.models import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    curso = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
    orientadores = models.ManyToManyField('docentes.Docente', related_name='alunos_orientados')
    defesa = models.BooleanField(default=False)
    data_defesa = models.DateField(null=True)
    artigo = models.URLField(max_length=400, null=True, blank=True)
    bolsista = models.CharField(max_length=255)
    obs = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    matricula = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

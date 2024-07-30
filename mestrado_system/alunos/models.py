from django.db import models
from turmas.models import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
    orientadores = models.ManyToManyField('docentes.Docente', related_name='alunos_orientados')
    defesa = models.BooleanField(blank=True)
    data_defesa = models.DateField(null=True, blank=True)
    artigo = models.CharField(max_length=255, null=True, blank=True)
    eh_bolsista = models.BooleanField(default=False, blank=True)
    nome_da_bolsa = models.CharField(max_length=30, null=True, blank=True)
    obs = models.TextField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, null=True)
    matricula = models.CharField(max_length=20, null=True)
    academico = models.URLField(max_length=255, null=True, blank=True)

    SITUACAO_CHOICES = [
        ("E", "Em andamento"),
        ("J", "Jubilado"),
        ("D", "Desistência"),
        ("T", "Trancamento"),
        ("C", "Concluído"),
    ]

    situacao = models.CharField(max_length=2, choices=SITUACAO_CHOICES, default='E')
    motivo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
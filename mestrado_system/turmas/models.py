from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    vagas = models.IntegerField(null=True)
    curso = models.CharField(max_length=255)
    data_de_inicio = models.DateField(null=True)
    data_de_criação = models.DateField(null=True)

from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    orientador1 = models.CharField(max_length=255)
    orientador2 = models.CharField(max_length=255)
    bolsista = models.CharField(max_length=255)
    obs = models.TextField()
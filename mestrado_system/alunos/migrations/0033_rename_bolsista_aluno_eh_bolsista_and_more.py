# Generated by Django 4.2.11 on 2024-07-11 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0032_aluno_academico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='bolsista',
            new_name='eh_bolsista',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='bolsa',
            new_name='nome_da_bolsa',
        ),
    ]

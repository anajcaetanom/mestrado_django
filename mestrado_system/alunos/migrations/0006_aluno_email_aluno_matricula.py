# Generated by Django 4.2.9 on 2024-02-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_alter_aluno_orientador2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
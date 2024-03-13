# Generated by Django 4.2.10 on 2024-03-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0015_alter_aluno_artigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='artigo',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='obs',
            field=models.TextField(max_length=255),
        ),
    ]

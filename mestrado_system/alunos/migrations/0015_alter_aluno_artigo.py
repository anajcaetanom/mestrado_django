# Generated by Django 4.2.10 on 2024-03-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0014_alter_aluno_defesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='artigo',
            field=models.URLField(blank=True, null=True),
        ),
    ]

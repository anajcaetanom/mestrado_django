# Generated by Django 4.2.11 on 2024-04-10 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0026_desistente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ativos',
            fields=[
                ('aluno_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alunos.aluno')),
                ('estado', models.TextField(verbose_name='Aluno ativo.')),
            ],
            bases=('alunos.aluno',),
        ),
    ]

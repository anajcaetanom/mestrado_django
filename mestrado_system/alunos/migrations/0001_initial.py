# Generated by Django 4.2.9 on 2024-02-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('orientador1', models.CharField(max_length=255)),
                ('orientador2', models.CharField(max_length=255)),
                ('bolsista', models.CharField(max_length=255)),
                ('obs', models.TextField()),
            ],
        ),
    ]

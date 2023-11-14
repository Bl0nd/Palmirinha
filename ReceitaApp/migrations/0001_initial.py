# Generated by Django 4.2.7 on 2023-11-08 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ingredientes', models.TextField(max_length=2000)),
                ('preparo', models.TextField(max_length=8000)),
                ('dificuldade', models.CharField(max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReceitaApp.categoria')),
            ],
        ),
    ]

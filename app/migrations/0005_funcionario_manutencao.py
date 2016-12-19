# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_equipamento_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Equipamento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Funcionario')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('fabricante', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='equipamento',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Status'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_funcionario_manutencao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

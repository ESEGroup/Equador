# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_manutencao_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manutencao',
            name='data_fim',
            field=models.DateTimeField(null=True),
        ),
    ]
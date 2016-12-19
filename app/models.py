from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Status(models.Model):

	id = models.AutoField(primary_key = True)
	nome = models.CharField(max_length=200)


class Equipamento(models.Model):

	nome = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	status = models.ForeignKey('Status', on_delete=models.CASCADE)

class Manutencao(models.Model):

	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	equipamento = models.ForeignKey('Equipamento')
	funcionario = models.ForeignKey('Fucionario')
	
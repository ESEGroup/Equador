#from __future__ import unicode_literals

from django.db import models

from datetime import date 

from django.contrib.auth.models import AbstractUser

class Departamento(models.Model):
	nome = models.CharField(max_length=200)	

class StatusEquipamento(models.Model):
	nome = models.CharField(max_length=200)


class Equipamento(models.Model):

	nome = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	status = models.ForeignKey('StatusEquipamento', on_delete=models.CASCADE)
	departamento = models.ForeignKey('Departamento')

	def __str__(self):
		return self.nome


class Usuario(AbstractUser):
	username = models.CharField(max_length=40, unique=True)
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	cpf = models.IntegerField()
	profissao = models.CharField(max_length=100, choices=[("0", "AdmGeral"),("1", "AdmDep"), ("2", "Funcionario")])
	departamento = models.ForeignKey('Departamento')

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['cpf','profissao','email','departamento']

	def __str__(self):
		return self.nome
	

class Manutencao(models.Model):

	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField(null=True)
	equipamento = models.ForeignKey('Equipamento')
	status = models.ForeignKey('StatusManutencao')
	responsavel = models.ForeignKey('Usuario')


class StatusManutencao(models.Model):
	nome = models.CharField(max_length=200)
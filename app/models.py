#from __future__ import unicode_literals

from django.db import models

from enum import Enum 
from datetime import date 

# Create your models here.

class Status(models.Model):

	nome = models.CharField(max_length=200)


class Equipamento(models.Model):

	nome = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	status = models.ForeignKey('Status', on_delete=models.CASCADE)


class Listas(Equipamento):

	listaequipamentos = models.ManyToManyField()

class Usuario(models.Model):
	nome = models.CharField(max_lenght=100)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(choices=["AdmGeral","AdmDep", "FuncioMan"])

	def selecionarUsu():
		return nome 
		

class Administrador(Usuario):
	departamento = models.CharField ()


	def retonaDep():
		return departamento

class Funcionario(Usuario):


class Manutencao(models.Model):

	Hoje = date.today()
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	equipamento = models.ForeignKey('Equipamento')
	funcionario = models.ForeignKey('Funcionario')
	
	def verificar():
		if Hoje>=data_inicio and Hoje<=data_fim:
			equipamento.status= "Em Manutencao"
		elif hoje < data_fim:
			equipamento.status= "Manutencao Pendente"
		else
			equipamento.status= "Disponivel"

		return equipamento.status 


	def concluirManutencao():
		data_fim = Hoje



	


 	
	''''nome = models.CharField(max_lenght=30)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(Profissao)
'''

'''	def mostradados():
		print(nome)
		print(cpf)
		print(profissao)'''



	

>>>>>>> 07b9db94da716da570215600257b736f406df6e3

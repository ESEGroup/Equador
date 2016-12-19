#from __future__ import unicode_literals

from django.db import models

#from enum import Enum 
from datetime import date 

# Create your models here.

class Status(models.Model):

	id = models.AutoField(primary_key = True)
	nome = models.CharField(max_length=200)


class Equipamento(models.Model):

	nome = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	status = models.ForeignKey('Status', on_delete=models.CASCADE)


class ListaEquip(models.Model):

	listaequipamentos = models.ManyToManyField('Equipamento')

	quantidadeEquip = lenght(listaequipamentos)

	def exibir():

		for i in range (0,quantidadeEquip):
			print listaequipamentos[i]

		return

class Usuario(models.Model):
	nome = models.CharField(max_lenght=100)
	cpf = models.IntegerField()
	profissao = models.CharField(choices=["AdmGeral","AdmDep", "FuncioMan"])

	def selecionarUsu():
		return nome 
		

class Administrador(Usuario):
	departamento = models.CharField ()


	def retonaDep():
		return departamento

class Funcionario(Usuario):

	def notificar():

class Manutencao(models.Model):

	Hoje = date.today()
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	equipamento = models.ForeignKey('Equipamento')
	funcionario = models.ForeignKey('Fucionario')
	
	def verificar():
		if Hoje>=data_inicio and Hoje<=data_fim:
			equipamento.status= "Em Manutencao"
		elif Hoje < data_fim:
			equipamento.status= "Manutencao Pendente"
		else
			equipamento.status= "Disponivel"

		return equipamento.status 


	def concluirManutencao():
		data_fim = Hoje

		return

class ListaManut():
	listamanutencao = models.ManyToManyField('Manutencao')
	quantidadeManut = lenght(listamanutencao)
	
	def exibir():

		for i in range (0,quantidadeManut):
			print listamanutencao[i]

		return

	


 	
	''''nome = models.CharField(max_lenght=30)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(Profissao)
'''

'''	def mostradados():
		print(nome)
		print(cpf)
		print(profissao)'''



	


#from __future__ import unicode_literals

from django.db import models

from enum import Enum 

# Create your models here.

	

class Usuario(models.Model):
	nome = models.CharField(max_lenght=100)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(choices=["AdmGeral","AdmDep", "FuncioMan"])

	def selecionar():
		return nome 
		

class Administrador(Usuario):
	departamento = models.CharField ()


	def 

class Funcionario(Usuario):

class RequisicaoManut():
	codigoDeManutencao = models.CharField(max_lenght=10)



	''''nome = models.CharField(max_lenght=30)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(Profissao)
'''

'''	def mostradados():
		print(nome)
		print(cpf)
		print(profissao)


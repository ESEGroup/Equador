#from __future__ import unicode_literals

from django.db import models

#from enum import Enum 
from datetime import date 

# Create your models here.




class View_Manutencao():

	def novaManut(Funcionario, Equipamento):
		manut = Manutencao()

		
		manut.funcionario = Funcionario
		manut.equipamento = Equipamento
		notificar(Funcionario, Equipamento)


		return

	def notificar (Funcio, Equip): #CONFERIR
		print ("%s deve realizar manutencao de %s", Funcio, Equip)

		return

class Status(models.Model):

	nome = models.CharField(max_length=200)


class Equipamento(models.Model):

	nome = models.CharField(max_length=200)
	fabricante = models.CharField(max_length=200)
	status = models.ForeignKey('Status', on_delete=models.CASCADE)
	local = models.CharField(max_length=200)

class ListaEquip(models.Model):

	listaequipamentos = models.ManyToManyField('Equipamento')

	quantidadeEquip = lenght(listaequipamentos)

	def exibir():

		for i in range (0,quantidadeEquip):
			print listaequipamentos[i]

		return


class Usuario(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.IntegerField()



	profissao = models.CharField(max_length=100, choices=[("0", "AdmGeral"),("1", "AdmDep"), ("2", "FuncioMan")])


	def selecionarUsuario():
		return nome 
		

class Administrador(Usuario):
	departamento = models.CharField (max_length=200)


	def retonaDep():
		return departamento

class Funcionario(Usuario):
	pass

	def notificar():
	
	


class Manutencao(models.Model):

	Hoje = date.today()
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	equipamento = models.ForeignKey('Equipamento')
	funcionario = models.ForeignKey('Funcionario')
	
	def verificar():
		if Hoje>=data_inicio and Hoje<=data_fim:
			equipamento.status= "Em Manutencao"
		elif Hoje < data_fim:
			equipamento.status= "Manutencao Pendente"
		else:
			equipamento.status= "Disponivel"

		return equipamento.status 


	def concluirManutencao():
		data_fim = Hoje

		return


	def EscolherData(manut, inicio, fim):#A CONFERIR
		
		for dia in range(lista_dias_ocupados[0].day, fim.day):
			if dataocupada[i]>= inicio and dataocupada[i]<= fim:
				return "data ocupada"

			dia= lista_dias_ocupados[i+1]		

		manut.data_inicio= inicio
		manut.data_fim= fim

		return



class ListaManut():
	listamanutencao = models.ManyToManyField('Manutencao')
	quantidadeManut = lenght(listamanutencao)
	
	def exibir():

		for i in range (0,quantidadeManut):
			print listamanutencao[i]

		return

	def exibirManFunc(nome):
		ans = []
		for i in range (0,quantidadeManut):
			if listamanutencao[i].funcionario.nome==nome:
				ans.append(listamanutencao[i])
		return ans


	


 	
	''''nome = models.CharField(max_lenght=30)
	cpf = models.IntegerField()
	profissao = models.ForeignKey(Profissao)
'''

'''	def mostradados():
		print(nome)
		print(cpf)
		print(profissao)'''

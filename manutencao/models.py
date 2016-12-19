from django.db import models
from equipamento.models import Equipamento

# Create your models here.

class Funcionario(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateTimeField()

	def __str__(self):
		return self.nome

class Manutencao(models.Model):
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	equipamento = models.ForeignKey(Equipamento)
	funcionario = models.ForeignKey(Funcionario)

	def __str__(self):
		ans = self.funcionario.nome + " - " + self.equipamento.tipo.nome
		return ans


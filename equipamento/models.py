from django.db import models

# Create your models here.

class TipoEquipamento(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return str(self.id) + " - " + self.nome

class Status(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Equipamento(models.Model):
	tipo = models.ForeignKey(TipoEquipamento,
							on_delete=models.CASCADE,
							default=1)
	fabricante = models.CharField(max_length=200,
							default="Fabricante default")
	image = models.CharField(max_length=1000)
	status = models.ForeignKey(Status, on_delete=models.CASCADE,
							default=1)

	def __str__(self):
		return str(self.id) + " - " + self.tipo.nome

	def datas_ocupadas(self):
		ans = []
		for manut in self.manutencao_set.all():
			ans += (manut.inicio, manut.fim)


"""
class ListaEquipamento(models.Model):

	def __str__(self):
		ans = ""
		for elemento in self.elementolista_set.all():
			ans += elemento.equipamento.tipo.nome + ', '
		else:
			ans = ans[:-2]
		return ans
"""

# >>> l1 = ListaEquipamento.objects.get(id=1)
# >>> l1.elementolista_set.all()
# <QuerySet [<ElementoLista: ElementoLista object>, <ElementoLista: ElementoLista object>]>
# >>> equip1 = Equipamento.objects.get(id=1)
# >>> l1.elementolista_set.create(equipamento=equip1)
# #### Todos os atributos exceto a chave estrangeira para essa classe
# Acho que não precisa dar save depois
# >>> l1.elementolista_set.count()

"""
class ElementoLista(models.Model):
	equipamento = models.ForeignKey(Equipamento, 
									on_delete=models.CASCADE)
	lista = models.ForeignKey(ListaEquipamento,
									on_delete=models.CASCADE)
"""

# No shell:
# python manage.py shell
# >>> from equipamento.models import Equipamento, ListaEquipamento, ElementoLista
# >>> Equipamento.objects.all()
# <QuerySet []>
# >>> # mostra os itens na tabela Equipamento
# >>> tipo1 = TipoEquipamento(nome = "Equipamento default")
# >>> tipo1.save()
# >>> tipo2 = TipoEquipamento(nome = "Ar condicionado")
# >>> tipo2.save()
# >>> equip1 = Equipamento(tipo=2, 
#	                  image="http://www.casasbahia-imagens.com.br/ArVentilacao/ArCondicionado/Janela/455919/5439647/Ar-Condicionado-Springer-Carrier-Duo-Mecanico-Frio-10-000-BTUs-455919.jpg")
# >>> equip1.save()
# >>> tipo2 = TipoEquipamento()
# >>> tipo2.nome = "Ventilador"
# >>> tipo2.save()
# >>> # salva no banco de dados
# >>> TipoEquipamento.objects.filter(id=1)
# Equipamento default
# >>> TipoEquipamento.objects.filter(id=3)
# []
# >>> TipoEquipamento.objects.filter(nome__startswith="Ar")
# [<TipoEquipamento: 2 - Ar condicionado>]
from django import forms
from app.models import *

class ManutencaoForm(forms.Form):
    equipamentos = forms.ModelChoiceField(queryset=Equipamento.objects.filter(status=1).order_by('nome'), to_field_name='nome')
    responsavel = forms.ModelChoiceField(queryset=Usuario.objects.filter(profissao=2).order_by('nome'), to_field_name='nome')

class EquipamentoForm(forms.Form):
	nome = forms.CharField(max_length=200)
	fabricante = forms.CharField(max_length=200)
	status = forms.ModelChoiceField(queryset=StatusEquipamento.objects.all().order_by('nome'), to_field_name='nome')
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nome'), to_field_name='nome')

class UsuarioForm(forms.Form):
	username = forms.CharField(max_length=200)
	senha = forms.CharField(max_length=200)
	nome = forms.CharField(max_length=200)
	email = nome = forms.CharField(max_length=200)
	cpf = forms.IntegerField()
	profissao = forms.ChoiceField([("0", "AdmGeral"),("1", "AdmDep"), ("2", "Funcionario")])
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all().order_by('nome'), to_field_name='nome')
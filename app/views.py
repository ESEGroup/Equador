from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.http import HttpResponse
from app.models import *
from app.forms import *
import datetime
# Create your views here.

def index(request):
	auth_form = AuthenticationForm()
	context = {'form': auth_form}
	return render(request,'index.html', context)

def login(request):
	username = request.POST['username']
	pw = request.POST['password']
	usuario = authenticate(username=username, password=pw)
	if usuario is not None:
		authlogin(request=request, user=usuario)
		# Redirect to a success page.
		print('ok')
		return redirect('home')
	else:
		# Return an 'invalid login' error message.
		form = AuthenticationForm(request.POST or None)
		print('not ok')
		return render(request, 'index.html', {'form' : form, 'erro' : True })

def logout(request):
	authlogout(request)
	return redirect('index')

@login_required(login_url='')
def home(request):
	equipamentos = Equipamento.objects.all()
	context = {'equipamentos': equipamentos}
	return render(request,'home.html', context)

@login_required(login_url='')
def manutencao(request):
	manutencoes = Manutencao.objects.filter(equipamento__departamento=request.user.departamento)
	if request.user.profissao == 'Funcionario':
		manutencoes.filter(responsavel=request.user)
	context = {'manutencoes': manutencoes}
	return render(request,'manutencoes.html', context)

@permission_required('app.can_add_manutencao', login_url='')
def manutencaoCriar(request):
	if request.method == 'POST':
		form = ManutencaoForm(request.POST)
		if form.is_valid():
			eqp = form.cleaned_data['equipamentos']
			responsavel = form.cleaned_data['responsavel']
			Manutencao.objects.create(equipamento=eqp, responsavel=responsavel, data_inicio=datetime.datetime.now(), data_fim=None, status=StatusManutencao.objects.filter(nome='pendente').first())

			equip = Equipamento.objects.get(pk=eqp.pk)
			equip.status = StatusEquipamento.objects.get(pk=2)
			equip.save()

			return redirect('manutencao')
    
	form = ManutencaoForm()
	context = {'form' : form}
	return render(request,'manutencoes_criar.html', context)

@permission_required('app.can_add_equipamento', login_url='')
def equipamentoCriar(request):
	if request.method == 'POST':
		form = EquipamentoForm(request.POST)
		if form.is_valid():
			nome = form.cleaned_data['nome']
			fabricante = form.cleaned_data['fabricante']
			status = form.cleaned_data['status']
			departamento = form.cleaned_data['departamento']

			Equipamento.objects.create(nome=nome, fabricante=fabricante, status=status, departamento=departamento)

			return redirect('home')
    
	form = EquipamentoForm()
	context = {'form' : form}
	return render(request,'equipamento_criar.html', context)

@permission_required('app.can_add_usuario', login_url='')
def usuarioCriar(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			senha = form.cleaned_data['senha']
			nome = form.cleaned_data['nome']
			email = form.cleaned_data['email']
			cpf = form.cleaned_data['cpf']
			profissao = form.cleaned_data['profissao']
			departamento = form.cleaned_data['departamento']

			Usuario.objects.create_user(username=username, password=senha, nome=nome,email=email,cpf=cpf,profissao=profissao, departamento=departamento)

			return redirect('home')
    
	form = UsuarioForm()
	context = {'form' : form}
	return render(request,'usuario_criar.html', context)
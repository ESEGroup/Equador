from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Manutencao

# Create your views here.
def index(request):
	#template = loader.get_template('equipamento/index.html')
	all_manut = Manutencao.objects.all()
	context = {'all_manut': all_manut}
	return render(request, 'manutencao/index.html', context)

	#return HttpResponse(template.render(context, request))


def detail(request, manut_func):
	manutencoes = Manutencao.objects.filter(funcionario=manut_func)
	if not manutencoes:
		return HttpResponse("<h1> Não há manutenções para este funcionário </h1>")
	return render(request, 'manutencao/detail.html', {'manutencoes':manutencoes})

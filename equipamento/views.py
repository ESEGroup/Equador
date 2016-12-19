from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import loader
from .models import Equipamento, TipoEquipamento

# Create your views here.

def index(request):
	#template = loader.get_template('equipamento/index.html')
	all_equips = Equipamento.objects.all()
	context = {'all_equips': all_equips}
	return render(request, 'equipamento/index.html', context)

	#return HttpResponse(template.render(context, request))


def detail(request, equip_id):
	try:
		equip = Equipamento.objects.get(id=equip_id)
	except Equipamento.DoesNotExist:
		raise Http404("Equipamento não existe")
	return render(request, 'equipamento/detail.html', {'equip':equip})


# No html:
# código: {% codigo aqui %}
# variável: { variavel aqui }
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

# Create your views here.

def index(request):
	#template = loader.get_template('equipamento/index.html')
	return render(request, 'home/index.html')

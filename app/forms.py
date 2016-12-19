from django import forms
from app.models import *

class ManutencaoForm(forms.Form):
    equipamentos = forms.ModelChoiceField(queryset=Equipamento.objects.filter(status=1).order_by('nome'), to_field_name='nome')
    responsavel = forms.ModelChoiceField(queryset=Usuario.objects.filter(profissao=2).order_by('nome'), to_field_name='nome')

from django.conf.urls import url
from . import views

app_name = 'manutencao'

urlpatterns = [
	# /manutencao/
    url(r'^$', views.index, name='index'),

    # /manutencao/<Funcionario_id>
    url(r'^(?P<manut_func>[0-9]+)/$', views.detail, name='detail')
]

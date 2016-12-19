from django.conf.urls import url
from . import views

app_name = 'equipamento'

urlpatterns = [
	# /equipamento/
    url(r'^$', views.index, name='index'),

    # /equipamento/1
    url(r'^(?P<equip_id>[0-9]+)/$', views.detail, name='detail')
]

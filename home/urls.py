from django.conf.urls import url
from . import views


app_name = 'homepage'

urlpatterns = [
	# /equipamento/
    url(r'^$', views.index , name='index'),

 ]

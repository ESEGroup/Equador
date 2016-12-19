from django.contrib import admin
from .models import Equipamento, TipoEquipamento, Status

# Register your models here.
admin.site.register(TipoEquipamento)
admin.site.register(Equipamento)
admin.site.register(Status)
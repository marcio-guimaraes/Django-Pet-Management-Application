from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bicho
class BichoAdmin(admin.ModelAdmin):
    list_display = ['nome_dono','caracteristicas']


admin.site.register(Bicho)
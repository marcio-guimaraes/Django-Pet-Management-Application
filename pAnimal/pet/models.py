from django.db import models
from django.utils import timezone
from ast import  Str


class Bicho(models.Model):
    nome_dono = models.CharField(max_length=120, null=False, blank=False)
    telefone = models.CharField(max_length=120, null=False, blank=False)
    nome_animal = models.CharField(max_length=120, null=False, blank=False)
    raca = models.CharField(max_length=120, null=False, blank=False)
    caracteristicas = models.CharField(max_length=1000,null=False,blank=False)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_dono


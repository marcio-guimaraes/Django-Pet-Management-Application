from django.db import models
from django.utils import timezone


class Bicho(models.Model):
    nome_dono = models.CharField(max_length=120, null=False, blank=False)
    telefone = models.CharField(max_length=120, null=False, blank=False)
    nome_animal = models.CharField(max_length=120, null=False, blank=False)
    raca = models.CharField(max_length=120, null=False, blank=False)
    caracteristicas = models.TextField(null=False)
    data = models.DateTimeField(default=timezone.now)
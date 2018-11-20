from django.db import models

from contas.models import Usuario

class Coordenador(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'

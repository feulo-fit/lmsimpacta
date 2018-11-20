from django.db import models

from contas.models import Usuario

class Professor(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)
    apelido = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
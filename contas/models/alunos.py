from django.db import models

from contas.models import Usuario

class Aluno(Usuario):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)
    ra = models.CharField(max_length=20, unique=True)
    foto = models.CharField(max_length=255, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
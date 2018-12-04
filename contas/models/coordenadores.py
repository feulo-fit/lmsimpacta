from django.db import models
from django.shortcuts import reverse

from contas.models import Usuario, Pessoa

class Coordenador(Pessoa, Usuario):

    class Meta:
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'
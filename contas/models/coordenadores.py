from django.db import models
from django.shortcuts import reverse

from contas.models import Usuario, Pessoa

class Coordenador(Pessoa, Usuario):

    def get_absolute_url(self):
        return reverse("admin:index")

    class Meta:
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'
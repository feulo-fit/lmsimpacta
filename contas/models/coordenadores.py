from django.db import models

from contas.models import Usuario, Pessoa

class Coordenador(Usuario, Pessoa):
    
    class Meta:
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'

from django.db import models
from django.utils import timezone

from contas.models import Coordenador

class Disciplina(models.Model):
    STATUS = (
        ("ABERTA", "Aberta"),
        ("FECHADA", "Fechada")
    )

    nome = models.CharField(max_length=255, unique=True)
    data = models.DateField(default=timezone.now, blank=True, null=True)
    status = models.CharField(max_length=50, default='ABERTA', blank=True, null=True, choices=STATUS)
    plano_ensino = models.TextField(max_length=500)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=500)
    habilidades = models.TextField(max_length=500)
    ementa = models.TextField(max_length=500)
    conteudo_programatico = models.TextField(max_length=500)
    bibliografia_basica = models.TextField(max_length=500)
    bibliografia_complementar = models.TextField(max_length=500)
    percentual_pratico = models.IntegerField()
    percentual_teorico = models.IntegerField()
    coordenador = models.ForeignKey(Coordenador, models.PROTECT)

    def __str__(self):
        return self.nome
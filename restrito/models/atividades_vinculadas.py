from django.db import models

from contas.models import Professor
from restrito.models import Atividade
from curriculo.models import DisciplinaOfertada

class AtividadeVinculada(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    rotulo = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    class Meta:
        unique_together = ("atividade", "disciplina_ofertada", "rotulo")
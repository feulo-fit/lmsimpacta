from django.db import models
from django.utils import timezone

from contas.models import Aluno, Professor
from restrito.models import AtividadeVinculada

class Entrega(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255)
    resposta = models.TextField(max_length=500)
    data_entrega = models.DateTimeField(default=timezone.now, editable=False, null=True, blank=True)
    status = models.CharField(max_length=20, default='Entregue', null=True, blank=True)
    professor = models.ForeignKey(Professor, default=None, null=True, blank=True ,on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    data_avaliacao = models.DateTimeField(default=None, null=True, blank=True)
    obs = models.TextField(max_length=500)

    class Meta:
        unique_together = ("aluno", "atividade_vinculada")
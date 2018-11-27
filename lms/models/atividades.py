from django.db import models
from django.utils import timezone

from contas.models import Professor, Aluno
from curriculo.models import DisciplinaOfertada

class Atividade(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=500, default=None, blank=True, null=True)
    conteudo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20)
    extras = models.CharField(max_length=250, default=None, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

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
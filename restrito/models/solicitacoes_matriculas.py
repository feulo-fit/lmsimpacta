from django.db import models
from django.utils import timezone

from contas.models import Aluno, Professor, Coordenador
from curriculo.models import DisciplinaOfertada

STATUS = (
    ('Solicitada', 'Solicitada'),
    ('Aprovada', 'Aprovada'),
    ('Reprovada', 'Reprovada')
)
class SolicitacaoMatricula(models.Model):
    aluno = models.ForeignKey(Aluno, models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, models.PROTECT, default=None, blank=True, null=True)
    data = models.DateField(default=timezone.now, blank=True, null=True, editable=False)
    status = models.CharField(max_length=50, default='Solicitada', blank=True, null=True, choices=STATUS)

    class Meta:
        verbose_name = 'solicitação de matrícula'
        verbose_name_plural = 'solicitações de matrícula'
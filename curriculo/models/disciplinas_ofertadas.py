from django.db import models

from contas.models import Coordenador, Professor
from curriculo.models import Curso, Disciplina, Turma

class DisciplinaOfertada(models.Model):
    coordenador = models.ForeignKey(Coordenador, models.PROTECT)
    curso = models.ForeignKey(Curso, models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, models.PROTECT)
    turma = models.ForeignKey(Turma, models.PROTECT)
    dt_inicio_matricula = models.DateField()
    dt_fim_matricula = models.DateField()
    professor = models.ForeignKey(Professor, models.PROTECT, default=None, blank=True, null=True)
    metodologia = models.TextField(max_length=500, default=None, blank=True, null=True)
    recursos = models.TextField(max_length=500, default=None, blank=True, null=True)
    criterio_avaliacao = models.TextField(max_length=500, default=None, blank=True, null=True)
    plano_aulas = models.TextField(max_length=500, default=None, blank=True, null=True)

    class Meta:
        unique_together = ("disciplina", "curso", "turma")

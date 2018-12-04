from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

from contas.models import Coordenador, Professor
from curriculo.models import Curso, Disciplina, Turma
from lmsimpacta.utils import get_semestre_atual

class DisciplinaOfertadaQuery(QuerySet):

    def disciplinas_aluno(self, aluno, ano, semestre):
        return self.annotate(num_alunos=models.Count(
            'solicitacaomatricula__aluno',
            filter=models.Q(solicitacaomatricula__status='Aprovada')
        )).filter(
            solicitacaomatricula__aluno=aluno,
            solicitacaomatricula__status='Aprovada',
            turma__semestre=semestre,
            turma__ano=ano
        )

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

    objects = DisciplinaOfertadaQuery.as_manager()

    def __str__(self):
        return "{}-{}-{}".format(self.curso.sigla, self.disciplina.nome, self.turma)

    class Meta:
        verbose_name = 'oferta de disciplina'
        verbose_name_plural = 'ofertas de disciplinas'
        unique_together = ("disciplina", "curso", "turma")

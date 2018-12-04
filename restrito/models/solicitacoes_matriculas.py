from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

from contas.models import Aluno, Professor, Coordenador
from curriculo.models import DisciplinaOfertada

STATUS = (
    ('Solicitada', 'Solicitada'),
    ('Aprovada', 'Aprovada'),
    ('Reprovada', 'Reprovada')
)
class SolicitacaoMatriculaQuery(QuerySet):

    def matriculas_aprovadas(self, aluno, ano, semestre):
        return self.annotate(num_alunos=models.Count(
            'aluno',
            filter=models.Q(status='Aprovada')
        )).filter(
            aluno=aluno,
            status='Aprovada',
            disciplina_ofertada__turma__semestre=semestre,
            disciplina_ofertada__turma__ano=ano
        )

class SolicitacaoMatricula(models.Model):
    aluno = models.ForeignKey(Aluno, models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, models.PROTECT, default=None, blank=True, null=True)
    data = models.DateField(default=timezone.now, blank=True, null=True, editable=False)
    status = models.CharField(max_length=50, default='Solicitada', blank=True, null=True, choices=STATUS)

    objects = SolicitacaoMatriculaQuery.as_manager()

    class Meta:
        verbose_name = 'solicitação de matrícula'
        verbose_name_plural = 'solicitações de matrícula'
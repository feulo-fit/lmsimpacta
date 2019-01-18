from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

from lmsimpacta.utils import get_semestre_atual

class SolicitacaoMatriculaQuery(QuerySet):

    def matriculas_anteriores(self, aluno):
        ano, semestre = get_semestre_atual()
        return self.filter(
            aluno=aluno,
        ).exclude(
            disciplina_ofertada__turma__ano=ano,
            disciplina_ofertada__turma__semestre=semestre
        )

    def matriculas_atuais(self, aluno):
        ano, semestre = get_semestre_atual()
        return self.filter(
            aluno=aluno,
            disciplina_ofertada__turma__semestre=semestre,
            disciplina_ofertada__turma__ano=ano
        )

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
    STATUS = (
        ('Solicitada', 'Solicitada'),
        ('Aprovada', 'Aprovada'),
        ('Reprovada', 'Reprovada')
    )

    aluno = models.ForeignKey("contas.Aluno", models.PROTECT)
    disciplina_ofertada = models.ForeignKey("curriculo.DisciplinaOfertada", models.PROTECT)
    coordenador = models.ForeignKey("contas.Coordenador", models.PROTECT, default=None, blank=True, null=True)
    data = models.DateField(default=timezone.now, blank=True, null=True, editable=False)
    status = models.CharField(max_length=50, default='Solicitada', blank=True, null=True, choices=STATUS)

    objects = SolicitacaoMatriculaQuery.as_manager()

    class Meta:
        verbose_name = 'solicitação de matrícula'
        verbose_name_plural = 'solicitações de matrícula'
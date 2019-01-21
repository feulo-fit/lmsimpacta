from django.db import models
from django.db.models import Prefetch
from django.db.models.query import QuerySet

from .entregas import Entrega

class AtividadeVinculadaQuerySet(QuerySet):

    def listar_atividades_turma(self, usuario, do):
        qs = self.filter(disciplina_ofertada=do)
        if usuario.tipo == 'A':
            qs.prefetch_related(
                Prefetch(
                    "entrega_set",
                    queryset=Entrega.objects.filter(aluno=usuario.aluno),
                    to_attr="entrega"
                )
            )
        elif usuario.tipo == 'P':
            qs.annotate(entregas=models.Count('entrega'))
        return qs

class AtividadeVinculada(models.Model):
    STATUS = (
        ('DISPONIBILIZADA','Disponibilizada'),
        ('ABERTA','Aberta'),
        ('FECHADA','Fechada'),
        ('ENCERRADA','Encerrada'),
        ('PRORROGADA','Prorrogada')
    )

    atividade = models.ForeignKey("restrito.Atividade",on_delete=models.PROTECT)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey("curriculo.DisciplinaOfertada", on_delete=models.PROTECT)
    rotulo = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    objects = AtividadeVinculadaQuerySet.as_manager()

    def __str__(self):
        return "{}-{}".format(self.rotulo, self.atividade if hasattr(self, "atividade") else '')

    class Meta:
        unique_together = ("atividade", "disciplina_ofertada", "rotulo")

from django.db import models
from django.utils import timezone

class Entrega(models.Model):
    STATUS = (
        ('ENTREGUE', 'Entregue'),
        ('CORRIGIDO', 'Corrigido')
    )

    aluno = models.ForeignKey("contas.Aluno", on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey("restrito.AtividadeVinculada", on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255)
    resposta = models.TextField(max_length=500)
    data_entrega = models.DateTimeField(default=timezone.now, editable=False, null=True, blank=True)
    status = models.CharField(max_length=20, default='ENTREGUE', null=True, blank=True, choices=STATUS)
    professor = models.ForeignKey("contas.Professor", default=None, null=True, blank=True ,on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    data_avaliacao = models.DateTimeField(default=None, null=True, blank=True)
    obs = models.TextField(max_length=500)

    def __str__(self):
        return '{} - {}'.format(self.aluno, self.titulo)

    class Meta:
        ordering = ['aluno']
        unique_together = ("aluno", "atividade_vinculada")
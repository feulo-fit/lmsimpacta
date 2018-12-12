from django.db import models

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

    def __str__(self):
        return "{}-{}".format(self.rotulo, self.atividade if hasattr(self, "atividade") else '')

    class Meta:
        unique_together = ("atividade", "disciplina_ofertada", "rotulo")
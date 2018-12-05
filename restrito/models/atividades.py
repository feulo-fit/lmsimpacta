from django.db import models

from contas.models import Professor

TIPO_ATIVIDADE = (
    ('RESPOSTA ABERTA', 'Resposta Aberta'),
    ('TESTE', 'Teste')
)


class Atividade(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=500, default=None, blank=True, null=True)
    conteudo = models.TextField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_ATIVIDADE)
    extras = models.CharField(max_length=250, default=None, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
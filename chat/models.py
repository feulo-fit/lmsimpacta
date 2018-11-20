from django.db import models
from django.utils import timezone

from contas.models import Aluno, Professor

class Mensagem(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    conteudo = models.TextField(max_length=500)
    status = models.CharField(max_length=100, default='Enviada', blank=True, null=True)
    data_envio = models.DateField(default=timezone.now, blank=True, null=True, editable=False)
    data_resposta = models.DateField(default=None, blank=True, null=True)
    resposta = models.TextField(max_length=500, default=None, blank=True, null=True)
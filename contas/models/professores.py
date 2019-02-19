from django.db import models
from django.urls import reverse

from datetime import date

from contas.models import Usuario, Pessoa
from lms.models import MensagemSemMatriculaException
from restrito.models import AtividadeVinculada, SolicitacaoMatricula

class Professor(Pessoa, Usuario):
    
    apelido = models.CharField(max_length=255)

    def vincula_atividade(self, atividade, disciplina_ofertada, data_inicio, data_fim, rotulo):
        av = AtividadeVinculada(professor=self,
                                atividade=atividade,
                                disciplina_ofertada=disciplina_ofertada,
                                data_inicio=data_inicio,
                                data_fim=data_fim,
                                rotulo=rotulo,
                                status = 'Aberta' if data_inicio >= date.today() else 'Disponibilizada')
        av.save()
        return av

    def get_absolute_url(self):
        return reverse("restrito:home")

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
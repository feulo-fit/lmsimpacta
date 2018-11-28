from django.db import models
from django.urls import reverse

from contas.models import Usuario, Pessoa

class Professor(Pessoa, Usuario):
    
    apelido = models.CharField(max_length=255)

    def envia_mensagem_aluno(self, aluno, assunto, referencia, conteudo):
        from lms.models import SolicitacaoMatricula
        qs = SolicitacaoMatricula.objects \
            .filter(disciplina_ofertada__professor=self) \
            .filter(aluno=aluno)

        if qs.count() < 1:
            raise MensagemSemMatriculaException()

        m = Mensagem(aluno=aluno, professor=self, assunto=assunto, referencia=referencia, conteudo=conteudo)
        m.save()
        return m

    def envia_mensagem_turma(self, disciplina_ofertada, assunto, referencia, conteudo):
        from lms.models import SolicitacaoMatricula
        mensagens = []
        qs = SolicitacaoMatricula.objects\
            .filter(disciplina_ofertada__professor = self)\
            .filter(disciplina_ofertada=disciplina_ofertada)

        if qs.count() < 1:
            raise MensagemSemMatriculaException()

        alunos = [matricula.aluno for matricula in qs]
        for aluno in alunos:
            m = Mensagem(aluno=aluno, professor=self, assunto=assunto, referencia=referencia, conteudo=conteudo)
            m.save()
            mensagens.append(m)

        return mensagens

    def vincula_atividade(self, atividade, disciplina_ofertada, data_inicio, data_fim, rotulo):
        from lms.models import AtividadeVinculada
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
        return reverse("restrito:area_professor")

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
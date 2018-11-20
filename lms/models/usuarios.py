from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
from lms.models import MensagemSemMatriculaException
from chat.models import Mensagem

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1), blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    celular = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True

class Coordenador(Usuario, Pessoa):
    pass

class Aluno(Usuario, Pessoa):
    ra = models.CharField(max_length=20, unique=True)
    foto = models.CharField(max_length=255, default=None, blank=True, null=True)

    @property
    def foto_url(self):
        if self.foto != None:
            fs = FileSystemStorage()
            return fs.url(self.foto)

        return None

    def upload_foto(self, foto):
        if foto != None and type(foto) == UploadedFile:
            fs = FileSystemStorage()
            self.foto = fs.save(foto.name, foto)
            return fs.url(self.foto)

        return None

    def envia_mensagem(self, professor, assunto, referencia, conteudo):
        from lms.models import SolicitacaoMatricula
        qs = SolicitacaoMatricula.objects\
            .filter(disciplina_ofertada__professor = professor)\
            .filter(aluno=self)

        if qs.count() < 1:
            raise MensagemSemMatriculaException()

        m = Mensagem(aluno=self, professor=professor, assunto=assunto, referencia=referencia, conteudo=conteudo)
        m.save()
        return m


class Professor(Usuario, Pessoa):
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






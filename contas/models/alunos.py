from datetime import datetime

from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile

from contas.models import Usuario, Pessoa
from lms.models import MensagemSemMatriculaException

def diretorio_aluno(instance, filename):
    return 'aluno/{0}/{1}'.format(instance.ra, filename)

class Aluno(Pessoa, Usuario):
    
    ra = models.CharField(max_length=20, unique=True)
    foto = models.ImageField(upload_to=diretorio_aluno, blank=True, null=True)
    
    def envia_mensagem(self, professor, assunto, referencia, conteudo):
        from restrito.models import SolicitacaoMatricula
        qs = SolicitacaoMatricula.objects\
            .filter(disciplina_ofertada__professor = professor)\
            .filter(aluno=self)

        if qs.count() < 1:
            raise MensagemSemMatriculaException()

        from chat.models import Mensagem
        m = Mensagem(aluno=self, professor=professor, assunto=assunto, referencia=referencia, conteudo=conteudo)
        m.save()
        return m

    def save(self, *args, **kwargs):
        if not self.ra:
            hoje = datetime.now()
            ano = (hoje.year % 1000).__str__()
            semestre = '1' if hoje.month <=6 else '2'
            ra_prefixo = ano + semestre
            
            ra_max = Aluno.objects.filter(ra__startswith=ra_prefixo).aggregate(models.Max('ra'))['ra__max']
            self.ra = (int(ra_max) + 1).__str__() if ra_max else ra_prefixo+'0001'
            self.tipo = 'A'
            self.set_password('123@mudar')

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("restrito:home")

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
        ordering = ['nome', 'ra']
        
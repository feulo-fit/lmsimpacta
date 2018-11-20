from datetime import datetime
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile

from contas.models import Usuario, Pessoa
from lms.models import MensagemSemMatriculaException

def diretorio_aluno(instance, filename):
    return 'aluno/{0}/{1}'.format(instance.ra, filename)

class Aluno(Usuario, Pessoa):
    
    ra = models.CharField(max_length=20, unique=True)
    #foto = models.CharField(max_length=255, default=None, blank=True, null=True)
    foto = models.ImageField(upload_to=diretorio_aluno, blank=True, null=True)
    
    ''' Verificar a necessidade com o ImageField
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
    '''

    def envia_mensagem(self, professor, assunto, referencia, conteudo):
        from lms.models import SolicitacaoMatricula
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
            self.ra = ra_max + 1 if ra_max else int(ra_prefixo+'0001')
            self.tipo = 'A'
            self.set_password('123@mudar')

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
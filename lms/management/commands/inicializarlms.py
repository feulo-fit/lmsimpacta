import os

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.core.management import call_command

from contas.models import Aluno, Coordenador, Professor, Usuario
from curriculo.models import Curso, Disciplina, Turma
from lmsimpacta.utils import get_semestre_atual

class Command(BaseCommand):
    help = 'Constrói a aplicação base com os dados iniciais'

    def handle(self, *args, **kwargs):
        print("Incializando projeto LMSImpacta")
        print()
        print()
        self.limpar_banco_atual(settings.DEBUG)
        print()
        print()
        self.fazer_migrations()        
        print()
        print()
        self.criar_admin()
        print()
        print()
        self.criar_alunos()
        print()
        print()
        self.criar_coordenadores()
        print()
        print()
        self.criar_professores()
        print()
        print()
        self.criar_curriculo()
        print()
        print()
        self.criar_turmas()

    def criar_admin(self):
        print("=========== ADMIN ============")
        print("==> Agora, vamos criar o admin com senha padrão")
        Usuario.objects.create_superuser(
            login="admin",
            password="admin123*"
        )
        print("==> Admin criado!")
        print("=========== Fim do ADMIN ===========")

    def criar_alunos(self):
        print("============ ALUNOS =============")
        print("==> Agora, vamos criar os 100 alunos com senha padrão")
        for i in range(1, 101):
            login = "aluno{}".format(i)
            nome = "Aluno {}".format(i)
            celular = 11123456000+i
            email = "aluno{}@teste.com".format(i)
            Aluno.objects.create(
                login=login,
                email=email,
                nome=nome,
                celular=celular,
                password="teste123*"
            )
        print("==> Alunos criados!")
        print("=========== Fim do ALUNOS ===========")

    def criar_coordenadores(self):
        print("============ COORDENADORES =============")
        print("==> Agora, vamos criar os 5 coordenadores com senha padrão")
        for i in range(1, 6):
            login = "coordenador{}".format(i)
            nome = "Coordenador {}".format(i)
            celular = 11123156000+i
            email = "coordenador{}@teste.com".format(i)
            Coordenador.objects.create(
                login=login,
                email=email,
                nome=nome,
                celular=celular,
                password="teste123*"
            )
        print("==> Coordenadores criados!")
        print("=========== Fim do COORDENADORES ===========")

    def criar_curriculo(self):
        print("============ CURRICULO =============")
        print("==> Agora, vamos carregar o currículo da Impacta")
        call_command("loaddata", 'data/curriculo.json', verbosity=0)
        print("==> Currículo carregado!")
        print("=========== Fim do CURRICULO ===========")

    def criar_professores(self):
        print("=========== PROFESSORES =============")
        print("==> Agora, vamos criar os 10 professores com senha padrão")
        for i in range(1, 11):
            login = "professor{}".format(i)
            nome = "Professor {}".format(i)
            celular = 11123457000+i
            email = "professor{}@teste.com".format(i)
            Professor.objects.create(
                login=login,
                email=email,
                nome=nome,
                celular=celular,
                password="teste123*"
            )
        print("==> Professores criados!")
        print("=========== Fim dos PROFESSORES ===========")

    def criar_turmas(self):
        print("=========== TURMAS =============")
        print("==> Agora, vamos criar as turmas")
        ano, semestre = get_semestre_atual()
        for letra in ['A','B','C','D','E']:
            Turma.objects.create(
                nome=letra,
                ano=ano,
                semestre=semestre
            )
        print("==> Turmas criadas!")
        print("=========== Fim dos TURMAS ===========")

    def fazer_migrations(self):  
        print("=========== MIGRATION's =============")
        print("==> Primeiro, vamos criar a estrutura do BD")
        call_command("migrate", verbosity=0)
        print("==> Banco criado!")
        print("=========== Fim do MIGRATION's ===========")

    def limpar_banco_atual(self, debug=False):
        print("======== Limpando Banco Atual =======")
        if debug:
            print("==> Projeto em DEBUG, removendo o sqlite3")
            os.remove("db.sqlite3")
        else:
            print("==> Projeto em produção, ainda não implementada essa parte.")
        print("======== Banco Atual Limpado ========")
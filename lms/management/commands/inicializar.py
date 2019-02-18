import os

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.core.management import call_command

from contas.models import Aluno, Usuario

class Command(BaseCommand):
    help = 'Constrói a aplicação base com os dados iniciais'

    def handle(self, *args, **kwargs):
        print("Incializando projeto LMSImpacta")
        print()
        print()
        self.limpando_banco_atual(settings.DEBUG)
        print()
        print()
        self.faz_migrations()        
        print()
        print()
        self.cria_admin()
        print()
        print()
        self.cria_alunos()


    def cria_admin(self):
        print("=========== SUPERUSER's =============")
        print("==> Agora, vamos criar o admin com senha padrão")
        Usuario.objects.create_superuser(
            login="admin",
            password="admin123*"
        )
        print("==> Admin criado!")
        print("=========== Fim do SUPERUSER's ===========")

    def cria_alunos(self):
        print("=========== ALUNOS's =============")
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
            #print("Adicionado",login)
        print("==> Alunos criados!")
        print("=========== Fim do ALUNOS's ===========")


    def faz_migrations(self):  
        print("=========== MIGRATION's =============")
        print("==> Primeiro, vamos criar a estrutura do BD")
        call_command("migrate", verbosity=0)
        print("==> Banco criado!")
        print("=========== Fim do MIGRATION's ===========")

    def limpando_banco_atual(self, debug=False):
        print("======== Limpando Banco Atual =======")
        if debug:
            print("==> Projeto em DEBUG, removendo o sqlite3")
            os.remove("db.sqlite3")
        else:
            print("==> Projeto em produção, ainda não implementada essa parte.")
        print("======== Banco Atual Limpado ========")
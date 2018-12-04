from django.utils import timezone

def checa_aluno(usuario):
    return usuario.tipo == 'A'

def checa_professor(usuario):
    return usuario.tipo == 'P'

def checa_nao_coordenador(usuario):
    return checa_aluno(usuario) or checa_professor(usuario)

def get_semestre_atual():
    hoje = timezone.now()
    ano = hoje.year
    mes = hoje.month
    return ano, 1 if mes <=6 else 2

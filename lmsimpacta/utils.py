from django.utils import timezone

def get_semestre_atual():
    hoje = timezone.now()
    ano = hoje.year
    mes = hoje.month
    return ano, 1 if mes <=6 else 2

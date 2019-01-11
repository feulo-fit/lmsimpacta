from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from curriculo.models import DisciplinaOfertada as DO
from lmsimpacta.utils import checa_aluno, get_semestre_atual

@login_required
@user_passes_test(checa_aluno)
def home_aluno(request):
    ano, semestre = get_semestre_atual()
    cursos = DO.objects.disciplinas_aluno(
        request.user.aluno,
        ano,
        semestre
    )
    context = {
        'ano': ano,
        'semestre': semestre,
        'cursos_atuais': cursos
    }
    return render(request, 'restrito/home.html', context)

@login_required
@user_passes_test(checa_aluno)
def turma_aluno(request, id_do):
    do = get_object_or_404(DO, id=id_do)
    context = {
        'turma': do,
        'alunos': Aluno.objects.filter(
            solicitacaomatricula__disciplina_ofertada=do,
            solicitacaomatricula__status='Aprovada'
        ),
        'atividades':AtividadeVinculada.objects.filter(disciplina_ofertada=do)
    }
    return render(request, 'restrito/turma.html', context)


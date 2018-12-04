from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from contas.models import Aluno
from curriculo.models import DisciplinaOfertada as DO
from restrito.models import SolicitacaoMatricula as SO
from lmsimpacta.utils import get_semestre_atual

@login_required
def area_aluno(request):
    ano, semestre = get_semestre_atual()
    context = {
        'ano': ano,
        'semestre': semestre,
        'cursos_atuais': DO.objects.disciplinas_aluno(
            request.user.aluno,
            ano,
            semestre
        )
    }
    return render(request, 'restrito/area_aluno.html', context)

@login_required
def turma_aluno(request, id):
    do = get_object_or_404(DO, id=id)
    context = {
        'turma': get_object_or_404(DO, id=id),
        'alunos': Aluno.objects.filter(
            solicitacaomatricula__disciplina_ofertada=do,
            solicitacaomatricula__status='Aprovada'
        )
    }
    return render(request, 'restrito/turma_aluno.html', context)

@login_required
def area_professor(request):
    context = {}
    return render(request, 'restrito/area_professor.html', context)
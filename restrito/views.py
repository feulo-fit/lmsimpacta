from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from curriculo.models import DisciplinaOfertada as DO
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
def area_professor(request):
    context = {}
    return render(request, 'restrito/area_professor.html', context)
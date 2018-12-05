from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from contas.models import Aluno
from curriculo.models import DisciplinaOfertada as DO
from restrito.forms import AtividadeForm, AtividadeVinculadaForm
from restrito.models import (SolicitacaoMatricula as SO, Atividade, AtividadeVinculada)
from lmsimpacta.utils import get_semestre_atual, checa_nao_coordenador, checa_professor

@login_required
@user_passes_test(checa_nao_coordenador)
def home(request):
    ano, semestre = get_semestre_atual()
    if request.user.tipo == 'A':
        cursos = DO.objects.disciplinas_aluno(
            request.user.aluno,
            ano,
            semestre
        )
    else:
        cursos = DO.objects.disciplinas_professor(
            request.user.professor,
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
@user_passes_test(checa_nao_coordenador)
def turma(request, id_do):
    do = get_object_or_404(DO, id=id_do)
    context = {
        'turma': do,
        'alunos': Aluno.objects.filter(
            solicitacaomatricula__disciplina_ofertada=do,
            solicitacaomatricula__status='Aprovada'
        )
    }
    return render(request, 'restrito/turma.html', context)

@login_required
@user_passes_test(checa_professor)
def atividades(request):
    context = {
        'atividades': Atividade.objects.filter(professor=request.user.professor)
    }
    return render(request, 'restrito/atividades_lista.html', context)

@login_required
@user_passes_test(checa_professor)
def atividades_form(request, id_do=None):
    context  = {}
    if id:
        atividade = get_object_or_404(Atividade, id=id)
        context['titulo'] = 'Alterando atividade '+atividade.titulo
    else:
        atividade = None
        context['titulo'] = 'Nova Atividade de Aula'
    form = AtividadeForm(request.POST or None, instance=atividade)

    if request.POST and form.is_valid():
        atividade = form.save(commit=False)
        atividade.professor = request.user.professor
        atividade.save()
        context['mensagem'] = {
            'texto':'Atividade {} com sucesso!'.format('alterada' if id else 'incluída'),
            'tipo': 'success'
        }
        return redirect('restrito:atividades', context)

    context['form'] = form
    return render(request, 'restrito/atividade_form.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_vinculada_form(request, id_do, id_vin=None):
    context  = {}
    do = get_object_or_404(DO, id=id_do)
    form = AtividadeVinculadaForm(request.POST or None)

    if request.POST and form.is_valid():
        atividade = form.save(commit=False)
        atividade.professor = request.user.professor
        atividade.save()
        context['mensagem'] = {
            'texto':'Atividade vinculada com sucesso!',
            'tipo': 'success'
        }
        return redirect('restrito:atividades', context)

    context['form'] = form
    return render(request, 'restrito/atividade_vinculada_form.html', context)

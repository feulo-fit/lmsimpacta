from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from lmsimpacta.utils import checa_professor

@login_required
@user_passes_test(checa_professor)
def home_professor(request):
    ano, semestre = get_semestre_atual()
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
@user_passes_test(checa_professor)
def turma_professor(request, id_do):
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

@login_required
@user_passes_test(checa_professor)
def atividade_professor(request):
    context = {
        'atividades': Atividade.objects.filter(professor=request.user.professor)
    }
    return render(request, 'restrito/atividades_lista.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_form_professor(request, id=None):
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
        nextUrl = request.POST.get("next", "")
        if nextUrl:
            return redirect(nextUrl)
        else:
            return redirect('restrito:atividades')

    context['form'] = form
    return render(request, 'restrito/atividade_form.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_remover_professor(request, id=None):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    return redirect('restrito:atividades')

@login_required
@user_passes_test(checa_professor)
def atividade_vinculada_form_professor(request, id_do, id_vin=None):
    context  = {}
    do = get_object_or_404(DO, id=id_do)
    if id_vin:
        vinc = get_object_or_404(AtividadeVinculada, id=id_vin)
    else:
        vinc = None

    form = AtividadeVinculadaForm(request.user.professor, request.POST or None, instance=vinc)
    if request.POST and form.is_valid():
        vinculada = form.save(commit=False)
        vinculada.professor = request.user.professor
        vinculada.disciplina_ofertada = do
        vinculada.status = 'DISPONIBILIZADA'
        vinculada.save()
        context['mensagem'] = {
            'texto':'Atividade vinculada com sucesso!',
            'tipo': 'success'
        }
        return redirect('restrito:turma', id_do=id_do)

    context['form'] = form
    return render(request, 'restrito/atividade_vinculada_form.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_vinculada_remover_professor(request, id_do, id_vin):
    atividade = get_object_or_404(AtividadeVinculada, id=id_vin)
    atividade.delete()
    return redirect('restrito:turma', id_do=id_do)

@login_required
@user_passes_test(checa_professor)
def entrega_listar_professor(request, id_do, id_vin):
    vinculada = get_object_or_404(AtividadeVinculada, id=id_vin)
    entregas = Entrega.objects.filter(atividade_vinculada=vinculada)
    context = {
        "entregas": entregas,
        "atividade": vinculada
    }
    return render(request, 'restrito/entregas_lista.html', context)

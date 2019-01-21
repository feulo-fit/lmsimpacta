from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from contas.models import Aluno
from curriculo.models import DisciplinaOfertada as DO
from restrito.forms import AtividadeForm, AtividadeVinculadaForm, EntregaAlunoForm, SolicitacaoMatriculaForm
from restrito.models import Atividade, AtividadeVinculada, Entrega, SolicitacaoMatricula as SM
from lmsimpacta.utils import checa_aluno, checa_professor, get_semestre_atual

@login_required
def home(request):
    ano, semestre = get_semestre_atual()
    cursos = DO.objects.disciplinas_semestre(
        request.user.perfil,
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
def turma(request, id_do):
    do = get_object_or_404(DO, id=id_do)
    context = {
        'turma': do,
        'alunos': Aluno.objects.filter(
            solicitacaomatricula__disciplina_ofertada=do,
            solicitacaomatricula__status='Aprovada'
        ),
        'atividades':AtividadeVinculada.objects.listar_atividades_turma(request.user, do)
    }
    return render(request, 'restrito/turma.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_lista(request):
    context = {
        'atividades': Atividade.objects.filter(professor=request.user.professor)
    }
    return render(request, 'restrito/atividade_lista.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_form(request, id=None):
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
        messages.success(request, 'Atividade {} com sucesso!'.format('alterada' if id else 'incluída'))
        nextUrl = request.POST.get("next", "")
        if nextUrl:
            return redirect(nextUrl)
        else:
            return redirect('restrito:atividade_lista')

    context['form'] = form
    return render(request, 'restrito/atividade_form.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_remover(request, id=None):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    messages.success(request, 'Atividade removida com sucesso!')
    return redirect('restrito:atividade_lista')

@login_required
@user_passes_test(checa_professor)
def atividade_vinculada_form(request, id_do, id_vin=None):
    context  = {}
    do = get_object_or_404(DO, id=id_do)
    if id_vin:
        vinc = get_object_or_404(AtividadeVinculada, id=id_vin)
        context["titulo"] = vinc.__str__()
    else:
        vinc = None
        context["titulo"] = 'Nova vinculação de atividade'

    form = AtividadeVinculadaForm(request.user.professor, request.POST or None, instance=vinc)
    if request.POST and form.is_valid():
        vinculada = form.save(commit=False)
        vinculada.professor = request.user.professor
        vinculada.disciplina_ofertada = do
        vinculada.status = 'DISPONIBILIZADA'
        vinculada.save()
        messages.success(request,'Atividade vinculada com sucesso!')
        return redirect('restrito:turma', id_do=id_do)

    context['form'] = form
    return render(request, 'restrito/atividade_vinculada_form.html', context)

@login_required
@user_passes_test(checa_professor)
def atividade_vinculada_remover(request, id_do, id_vin):
    atividade = get_object_or_404(AtividadeVinculada, id=id_vin)
    atividade.delete()
    messages.success(request,'Atividade vinculada removida com sucesso!')
    return redirect('restrito:turma', id_do=id_do)

@login_required
@user_passes_test(checa_professor)
def entrega_listar(request, id_do, id_vin):
    vinculada = get_object_or_404(AtividadeVinculada, id=id_vin)
    entregas = Entrega.objects.filter(atividade_vinculada=vinculada)
    context = {
        "entregas": entregas,
        "atividade": vinculada
    }
    return render(request, 'restrito/entrega_lista.html', context)

@login_required
@user_passes_test(checa_aluno)
def matricula_lista(request):
    ano, semestre = get_semestre_atual()
    context = {
        "ano": ano,
        "semestre": semestre,
        "matriculas": SM.objects.matriculas_atuais(request.user.aluno),
        "matriculas_anteriores": SM.objects.matriculas_anteriores(request.user.aluno)
    }

    return render(request, "restrito/matricula_lista.html", context)

@login_required
@user_passes_test(checa_aluno)
def matricula_solicitar(request, id_do=None):
    context = {}

    if id_do:
        SM.objects.create(
            aluno=request.user.aluno,
            disciplina_ofertada=DO.objects.get(id=id_do)
        )
        messages.success(request, "Matrícula solicitada com sucesso!")
        return redirect("restrito:matricula_lista")
    else:
        context["disciplinas"] = DO.objects.disciplinas_disponiveis(request.user.aluno)
    
    return render(request, "restrito/matricula_solicitar.html", context)

@login_required
@user_passes_test(checa_aluno)
def matricula_remover(request, id_sm):
    sm = get_object_or_404(SM,
        aluno=request.user.aluno,
        id=id_sm,
        status='Solicitada'
    )
    sm.delete()
    messages.success(request, "Matrícula cancelada com sucesso!")
    return redirect("restrito:matricula_lista")
    
@login_required
@user_passes_test(checa_aluno)
def entrega_form(request, id_do, id_vin, id_entrega=None):
    context = {}
    vinculada = get_object_or_404(AtividadeVinculada, id=id_vin)
    entrega = get_object_or_404(Entrega, id=id, aluno=request.user.aluno) if id_entrega else None
    form = EntregaAlunoForm(request.POST or None, instance=entrega)
    if request.POST and form.is_valid():
        entrega = form.save(commit=False)
        entrega.atividade_vinculada = vinculada
        entrega.aluno = request.user.aluno
        entrega.save()
        messages.success(request, 'Entrega realizada com sucesso!')
        return redirect('restrito:turma', id_do=id_do)
    context["form"] = form
    context['atividade'] = vinculada
    return render(request, 'restrito/entrega_form.html', context)
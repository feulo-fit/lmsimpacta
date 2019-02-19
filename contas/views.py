from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from contas.forms import LoginForm, AlunoCriacaoForm, AlunoAlteracaoForm, ProfessorAlteracaoForm

def entrar(request):
    context = {}
    form = LoginForm(request.POST or None)
    if request.POST:
        username = request.POST.get("login")
        senha = request.POST.get("senha")
        usuario = authenticate(request, login=username, password=senha)
        if usuario:
            login(request, usuario)
            return redirect(usuario.get_absolute_url())
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    context['form'] = form
    return render(request, 'contas/entrar.html', context)

def sair(request):
    logout(request)
    return redirect("lms:index")

def registrar(request):
    context = {}
    form = AlunoCriacaoForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, 'Registrado com sucesso!')
        return redirect("lms:index")

    context['form'] = form
    return render(request, 'contas/registrar.html', context)

def alterar_dados(request):
    context = {}
    usuario = request.user
    if usuario.tipo == 'A':
        form = AlunoAlteracaoForm(request.POST or None, request.FILES or None, instance=usuario.aluno)
    elif usuario.tipo == 'P':
        form = ProfessorAlteracaoForm(request.POST or None, instance=usuario.professor)
    else:
        return redirect('admin:password_change')
    
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, 'Dados alterados com sucesso')

    context['form'] = form
    return render(request, 'contas/alterar_dados.html', context)
from django.shortcuts import render

def area_aluno(request):
    context = {}
    return render(request, 'restrito/area_aluno.html', context)

def area_professor(request):
    context = {}
    return render(request, 'restrito/area_professor.html', context)
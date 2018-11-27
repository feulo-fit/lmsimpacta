from django.shortcuts import render, get_object_or_404

from curriculo.models import Curso

def curso(request, sigla):
    context = {
        'curso': get_object_or_404(Curso, sigla=sigla)
    }
    return render(request, 'curriculo/curso.html', context)
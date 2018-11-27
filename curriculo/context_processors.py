from curriculo.models import Curso

def lista_cursos(request):
    return {
        'cursos_menu': Curso.objects.all()
    }
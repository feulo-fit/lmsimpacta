from django.shortcuts import render

from .forms import ContatoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    context = {}
    form = ContatoForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.enviar_email()
            context['mensagem'] = {
                'texto':'Mensagem enviada com sucesso!',
                'tipo': 'success'
            }
        else:
            context['mensagem'] = {
                'texto': 'Problemas ao enviar a sua mensagem!',
                'tipo': 'danger'
            }
    context["form"] = form
    return render(request, 'contato.html', context)
from django.shortcuts import render

# Create your views here.
def mensagens(request):
    context = {}
    return render(request, "chat/mensagens.html", context)
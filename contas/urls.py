from django.urls import path

from . import views

app_name = 'contas'
urlpatterns = [
    path('entrar/', views.entrar, name='entrar'),
    path('sair/', views.sair, name='sair'),
    path('inscrever/', views.registrar, name='registrar'),
    path('alterar-dados/', views.alterar_dados, name='alterar')
]

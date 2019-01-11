from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('', views.home, name='home'),
    path('turma/<int:id_do>/', views.turma, name='turma'),
    path('turma/<int:id_do>/atividade/', views.atividade_vinculada_form, name='vinculada_form'),
    path('turma/<int:id_do>/atividade/<int:id_vin>/', views.atividade_vinculada_form, name='vinculada_form'),
    path('turma/<int:id_do>/atividade/<int:id_vin>/remover/', views.atividade_vinculada_remover, name='vinculada_remover'),
    path('turma/<int:id_do>/atividade/<int:id_vin>/entregas/', views.entrega_listar, name='entrega_lista'),
    path('turma/<int:id_do>/atividade/<int:id_vin>/entregar/', views.entrega_form, name='entrega_form'),
    path('atividades/', views.atividade_lista, name='atividade_lista'),
    path('atividades/form/', views.atividade_form, name='atividade_form'),
    path('atividades/form/<int:id>/', views.atividade_form, name='atividade_form'),
    path('atividades/remover/<int:id>/', views.atividade_remover, name='atividade_remover'),
    
]
from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('aluno/', views.home_aluno, name='home_aluno'),
    path('aluno/turma/<int:id_do>/', views.turma_aluno, name='turma_aluno'),
    path('aluno/turma/<int:id_do>/atividade/<int:id_vin>/entregar/', views.entrega_form_aluno, name='entrega_aluno'),

    path('professor/atividades/', views.atividade_professor, name='atividade_lista_professor'),
    path('professor/atividades/form/', views.atividade_form_professor, name='atividade_form_professor'),
    path('professor/atividades/form/<int:id>/', views.atividade_form_professor, name='atividade_form_professor'),
    path('professor/atividades/remover/<int:id>/', views.atividade_remover_professor, name='atividade_remover_professor'),
    path('professor/turma/<int:id_do>/', views.turma_professor, name='turma_professor'),
    path('professor/turma/<int:id_do>/atividade/', views.atividade_vinculada_form_professor, name='vinculada_form_professo'),
    path('professor/turma/<int:id_do>/atividade/<int:id_vin>/', views.atividade_vinculada_form_professor, name='vinculada_form_professor'),
    path('professor/turma/<int:id_do>/atividade/<int:id_vin>/remover/', views.atividade_vinculada_remover_professor, name='vinculada_remover_professor'),
    path('professor/turma/<int:id_do>/atividade/<int:id_vin>/entregas/', views.entrega_listar_professor, name='entrega_professor'),
]
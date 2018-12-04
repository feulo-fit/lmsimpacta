from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('aluno/', views.area_aluno, name='area_aluno'),
    path('aluno/disciplina/<int:id>/', views.turma_aluno, name='disciplina_aluno')
]
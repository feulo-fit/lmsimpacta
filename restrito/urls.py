from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('', views.home, name='home'),
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/form/', views.atividades_form, name='atividade_form'),
    path('atividades/form/<int:id>/', views.atividades_form, name='atividade_form'),
    path('turma/<int:id>/', views.turma, name='turma')
]
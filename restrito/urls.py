from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('', views.home, name='home'),
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/form/', views.atividades_form, name='atividade_form'),
    path('atividades/form/<int:id_do>/', views.atividades_form, name='atividade_form'),
    path('turma/<int:id_do>/', views.turma, name='turma'),
    path('turma/<int:id_do>/atividade/', views.atividade_vinculada_form, name='vinculada_form'),
    path('turma/<int:id_do>/atividade/<int:id_vin>/', views.atividade_vinculada_form, name='vinculada_form'),
]
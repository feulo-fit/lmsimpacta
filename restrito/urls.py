from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('', views.home, name='home'),
    path('atividades/', views.atividades, name='atividades'),
    path('turma/<int:id>/', views.turma, name='turma')
]
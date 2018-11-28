from django.urls import path

from . import views

app_name = 'restrito'
urlpatterns = [
    path('aluno/', views.area_aluno, name='area_aluno')
]
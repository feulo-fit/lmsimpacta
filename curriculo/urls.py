from django.urls import path

from . import views

app_name = 'curriculo'
urlpatterns = [
    path('<str:sigla>/', views.curso, name='curso')
]

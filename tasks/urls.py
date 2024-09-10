from django.urls import path
from .views import *

urlpatterns = [
    path('',  index, name='index'),
    path('criar_tarefa', criar_tarefa, name='criar_tarefa'),
    path('editar_tarefa/<int:id>', editar_tarefa, name='editar_tarefa'),
    path('deletar_tarefa/<int:id>', deletar_tarefa, name='deletar_tarefa')
]
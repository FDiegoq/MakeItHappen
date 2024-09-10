from django.shortcuts import render, redirect
from .models import *
from .form import TarefaModelForm
# Create your views here.

def index(request):
    tarefas=Tarefa.objects.all()
    context={
        'tarefas': tarefas
    }
    return render(request, 'index.html', context)

def criar_tarefa(request):
    form=TarefaModelForm()
    if request.method=='POST':
        form=TarefaModelForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('index')
    else:
        form=TarefaModelForm()

    return render(request, 'form.html', {'form': form})

def editar_tarefa(request, id):
    tarefa=Tarefa.objects.get(id=id)

    if request.method =='POST':
        form=TarefaModelForm(request.POST, instance=tarefa)
        if form.is_valid :
            form.save()
            return redirect('index')
    else:
        form=TarefaModelForm(instance=tarefa)
    

    return render(request, 'form.html', {'form' : form})

def deletar_tarefa(request, id):
    tarefa=Tarefa.objects.get(id=id)
    tarefa.delete()

    return redirect('index')

    
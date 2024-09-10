from django import forms
from .models import Tarefa
class TarefaModelForm(forms.ModelForm):
    class Meta():
        model=Tarefa
        fields='__all__'
        widgets={
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Digite o título da tarefa'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Descreva a tarefa'
            }),
            'status': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Status da tarefa (Ex: Pendente, Em andamento)'
            }),
            'setor': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'usuarios': forms.SelectMultiple(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }

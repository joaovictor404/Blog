from django.shortcuts import render
from .models import Curso, Modalidade, Aluno 
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos,
    }
    return render(request, 'cursos/index.html', contexto)

def detalhe_aluno(request, aluno_id):
    aluno_selecionado = Aluno.objects.get(id=aluno_id)
    contexto = {
        'aluno_selecionado': aluno_selecionado,
        }
    return render(request, 'cursos/detalhe_aluno.html', contexto)
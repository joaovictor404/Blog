from django.shortcuts import render
from .models import Curso, Modalidade, Aluno 
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos,
    }
    return render(request, 'cursos/index.html', contexto)

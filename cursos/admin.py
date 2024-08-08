from django.contrib import admin
from .models import Modalidade, Aluno, Curso
# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','cpf','email','data_nascimento',)
    search_fields = ('nome','idade','cpf','email','data_nascimento',)
    list_filter = ('nome','idade','cpf','email','data_nascimento',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','modalidade',)
    search_fields = ('nome','descricao',)
    list_filter = ('nome','descricao',)
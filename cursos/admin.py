from django.contrib import admin
from .models import Modalidade, Aluno, Curso
from django.utils.html import format_html
# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ('nome','idade','cpf','email','data_nascimento','image_tag',)
    search_fields = ('nome','idade','cpf','email','data_nascimento',)
    list_filter = ('nome','idade','cpf','email','data_nascimento',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao','modalidade',)
    search_fields = ('nome','descricao',)
    list_filter = ('nome','descricao',)
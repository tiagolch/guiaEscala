from django.contrib import admin
from .models import Funcao, Ministerio


@admin.register(Ministerio)
class MinisterioAdmin(admin.ModelAdmin):
    list_display = ['nome',
                    'ativo']
    list_editable = ['ativo']
    list_filter = ['ativo']
    search_fields = ['nome']


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ['funcao', 'ativo']
    list_editable = ['ativo']
    list_filter = ['ativo']
    search_fields = ['funcao']
    # autocomplete_fields = ['funcao']
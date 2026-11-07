
from django.contrib import admin
from .models import Ocorrencia


@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "bairro",
        "categoria",
        "status",
        "data_criacao",
    )

    list_filter = (
        "categoria",
        "status",
        "bairro",
    )

    search_fields = (
        "titulo",
        "bairro",
        "descricao",
    )

    readonly_fields = ("data_criacao",)


from django.urls import path
from . import views


app_name = "ocorrencias"

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "ocorrencias/",
        views.listar_ocorrencias,
        name="listar"
    ),

    path(
        "cadastrar/",
        views.cadastrar_ocorrencia,
        name="cadastrar"
    ),

    path(
        "painel/",
        views.painel,
        name="painel"
    ),
]

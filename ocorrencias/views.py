
from django.shortcuts import render, redirect

from .models import Ocorrencia
from .forms import OcorrenciaForm


def obter_estatisticas():
    return {
        "total": Ocorrencia.objects.count(),
        "pendentes": Ocorrencia.objects.filter(
            status="pendente"
        ).count(),
        "andamento": Ocorrencia.objects.filter(
            status="andamento"
        ).count(),
        "resolvidas": Ocorrencia.objects.filter(
            status="resolvido"
        ).count(),
    }


def home(request):
    contexto = obter_estatisticas()

    contexto["recentes"] = Ocorrencia.objects.all()[:3]

    return render(
        request,
        "ocorrencias/home.html",
        contexto
    )


def listar_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()

    categoria = request.GET.get("categoria", "")
    status = request.GET.get("status", "")

    if categoria:
        ocorrencias = ocorrencias.filter(
            categoria=categoria
        )

    if status:
        ocorrencias = ocorrencias.filter(
            status=status
        )

    contexto = {
        "ocorrencias": ocorrencias,
        "categorias": Ocorrencia.CATEGORIAS,
        "status_opcoes": Ocorrencia.STATUS,
        "categoria_selecionada": categoria,
        "status_selecionado": status,
    }

    return render(
        request,
        "ocorrencias/lista.html",
        contexto
    )


def cadastrar_ocorrencia(request):
    if request.method == "POST":
        formulario = OcorrenciaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("ocorrencias:listar")
    else:
        formulario = OcorrenciaForm()

    return render(
        request,
        "ocorrencias/cadastrar.html",
        {"formulario": formulario}
    )


def painel(request):
    contexto = obter_estatisticas()

    contexto["recentes"] = Ocorrencia.objects.all()[:6]

    return render(
        request,
        "ocorrencias/painel.html",
        contexto
    )

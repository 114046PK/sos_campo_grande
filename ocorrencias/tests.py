
from django.test import TestCase
from django.urls import reverse

from .models import Ocorrencia


class OcorrenciaTests(TestCase):

    def setUp(self):
        self.ocorrencia = Ocorrencia.objects.create(
            titulo="Buraco na avenida",
            descricao="Buraco próximo ao cruzamento",
            bairro="Centro",
            categoria="buraco",
        )

    def test_ocorrencia_criada(self):
        self.assertEqual(
            Ocorrencia.objects.count(),
            1
        )

    def test_status_inicial(self):
        self.assertEqual(
            self.ocorrencia.status,
            "pendente"
        )

    def test_pagina_inicial(self):
        resposta = self.client.get(
            reverse("ocorrencias:home")
        )

        self.assertEqual(resposta.status_code, 200)

    def test_cadastrar_ocorrencia(self):
        resposta = self.client.post(
            reverse("ocorrencias:cadastrar"),
            {
                "titulo": "Poste apagado",
                "descricao": "Rua sem iluminação",
                "bairro": "Tiradentes",
                "categoria": "iluminacao",
            }
        )

        self.assertEqual(resposta.status_code, 302)

        self.assertEqual(
            Ocorrencia.objects.count(),
            2
        )

    def test_filtrar_categoria(self):
        resposta = self.client.get(
            reverse("ocorrencias:listar"),
            {"categoria": "buraco"}
        )

        self.assertContains(
            resposta,
            "Buraco na avenida"
        )

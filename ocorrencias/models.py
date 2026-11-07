
from django.db import models


class Ocorrencia(models.Model):

    CATEGORIAS = [
        ("buraco", "Buraco na rua"),
        ("iluminacao", "Iluminação pública"),
        ("lixo", "Lixo irregular"),
        ("vazamento", "Vazamento de água"),
        ("outro", "Outro"),
    ]

    STATUS = [
        ("pendente", "Pendente"),
        ("andamento", "Em andamento"),
        ("resolvido", "Resolvido"),
    ]

    titulo = models.CharField(max_length=100)

    descricao = models.TextField(max_length=500)

    bairro = models.CharField(max_length=100)

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pendente"
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

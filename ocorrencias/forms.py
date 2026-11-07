
from django import forms
from .models import Ocorrencia


class OcorrenciaForm(forms.ModelForm):

    class Meta:
        model = Ocorrencia

        fields = [
            "titulo",
            "descricao",
            "bairro",
            "categoria",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: Buraco na avenida",
                }
            ),

            "descricao": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descreva o problema",
                }
            ),

            "bairro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex: Centro",
                }
            ),

            "categoria": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

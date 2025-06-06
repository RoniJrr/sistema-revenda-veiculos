from django import forms
from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'cor', 'quilometragem', 'preco', 'fipe', 'foto', 'destaque']

    def clean_quilometragem(self):
            quilometragem = self.cleaned_data['quilometragem']
            # Se for string (como '100.000'), remove ponto e converte pra int
            if isinstance(quilometragem, str):
                quilometragem = quilometragem.replace('.', '')
            return int(quilometragem)
from django import forms
from .models import Ferramenta, Manutencao


class DataInput(forms.DateInput):
    input_type = 'date'


class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = {'nome', 'numero_serie', 'data_compra'}
        widgets = {
            'data_compra': DataInput()
        }


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = {'data_manutencao', 'status_manutencao', 'observacoes', 'valor', 'numero_os'}
        widgets = {
            'data_manutencao': DataInput()
        }

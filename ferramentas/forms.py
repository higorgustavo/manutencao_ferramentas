from django import forms
from .models import Ferramenta, Manutencao


class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = {'nome', 'numero_serie', 'data_compra', 'observacoes'}
        widgets = {
            'data_compra': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'data_compra'}),
            'observacoes': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Se necessário escreva algo a respeito da ferramenta',
                       'id': 'observacoes', 'rows': 4}),
        }


class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = {'data_manutencao', 'local', 'status_manutencao', 'observacoes', 'valor', 'numero_os'}
        widgets = {
            'data_manutencao': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'date', 'id': 'data_manutencao'}),
            'observacoes': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Se necessário escreva algo a respeito da manutenção',
                       'id': 'observacoes', 'rows': 4}),
        }


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = {'data_manutencao', 'local'}
        widgets = {
            'data_manutencao': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'date', 'id': 'data_manutencao'}),
        }

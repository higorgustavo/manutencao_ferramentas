from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from ferramentas.models import Manutencao
from datetime import date


def dashboard(request):
    agendadas = Manutencao.objects.filter(status_manutencao="Agendada", data_manutencao__gte=date.today()).count()
    agendadas_hoje = Manutencao.objects.filter(status_manutencao="Agendada", data_manutencao=date.today()).count()
    concluidas = Manutencao.objects.filter(status_manutencao="Concluída").count()
    manutencoes_atrsadas = Q(
        Q(status_manutencao="Atrasada") | Q(status_manutencao="Agendada", data_manutencao__lt=date.today())
    )
    atrasadas = Manutencao.objects.filter(manutencoes_atrsadas).count()

    context = {
        "agendadas": agendadas,
        "agendadas_hoje": agendadas_hoje,
        "atrasadas": atrasadas,
        "concluidas": concluidas,
    }
    return render(request, "pages/dashboard.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from ferramentas.models import Manutencao
from datetime import date


def dashboard(request):

    agendadas = Manutencao.objects.filter(status_manutencao="Agendada").count()
    agendadas_hoje = Manutencao.objects.filter(status_manutencao="Agendada", data_manutencao=date.today()).count()
    concluidas = Manutencao.objects.filter(status_manutencao="Concluída").count()

    context = {
        "agendadas": agendadas,
        "agendadas_hoje": agendadas_hoje,
        "concluidas": concluidas
    }
    return render(request, "pages/dashboard.html", context)

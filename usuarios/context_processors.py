from ferramentas.models import Manutencao
from django.db.models import Q
from datetime import date


def manutencoes_atrasadas(request):
    agendadas_em_atraso = Q(status_manutencao="Agendada", data_manutencao__lt=date.today())
    atualizar_atrasadas = Manutencao.objects.filter(agendadas_em_atraso).update(status_manutencao="Atrasada")

    corecao_atrasadas = Q(status_manutencao="Atrasada", data_manutencao__gte=date.today())
    atualizar_agendadas = Manutencao.objects.filter(corecao_atrasadas).update(status_manutencao="Agendada")

    return {"atualizar_atrasadas": atualizar_atrasadas, "atualizar_agendadas": atualizar_agendadas}

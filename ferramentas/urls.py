from django.urls import path
from ferramentas.views.ferramenta_views import *
from ferramentas.views.manutencao_views import *

urlpatterns = [
    path("cliente/<int:id>/ferramenta/add", create_ferramenta, name='create_ferramenta'),
    path("ferramenta/<int:id>/", detail_ferramenta, name='detail_ferramenta'),
    path("ferramenta/<int:id>/update", update_ferramenta, name='update_ferramenta'),
    path("ferramenta/<int:id>/manutencao/add", create_manutencao, name='create_manutencao'),
    path("manutencao/<int:id>/visualizar", detail_manutencao, name='detail_manutencao'),
    path("manutencao/<int:id>/update", update_manutencao, name='update_manutencao'),
    path("ferramenta/<int:id>/agendamento", agendamento_rapido, name='agendamento_rapido'),
    path("manutencoes/agendadas", list_agendadas, name='list_agendadas'),
    path("manutencoes/agendadas-para-hoje", list_agendadas_hoje, name='list_agendadas_hoje'),
    path("manutencoes/atrasadas", list_atrasadas, name='list_atrasadas'),
    path("manutencoes/concluidas", list_concluidas, name='list_concluidas'),
    path("manutencoes/canceladas", list_canceladas, name='list_canceladas'),
]

from django.urls import path
from ferramentas.views.ferramenta_views import *
from ferramentas.views.manutencao_views import *

urlpatterns = [
    path("cliente/<int:id>/ferramenta/add", create_ferramenta, name='create_ferramenta'),
    path("ferramenta/<int:id>/", detail_ferramenta, name='detail_ferramenta'),
    path("ferramenta/<int:id>/update", update_ferramenta, name='update_ferramenta'),
    path("ferramenta/<int:id>/manutencao/add", create_manutencao, name='create_manutencao'),
    path("manutencao/<int:id>/visualizar", detail_manutencao, name='detail_manutencao'),
]

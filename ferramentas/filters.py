import django_filters
from .models import Manutencao


class ManutencaoFilter(django_filters.FilterSet):
    class Meta:
        model = Manutencao
        fields = ['local']

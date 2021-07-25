from django.urls import path
from .views import *

urlpatterns = [
    path("cliente/<int:id>/ferramenta/add", create_ferramenta, name='create_ferramenta'),
    path("ferramenta/<int:id>/", detail_ferramenta, name='detail_ferramenta'),
    path("ferramenta/<int:id>/update", update_ferramenta, name='update_ferramenta'),
]

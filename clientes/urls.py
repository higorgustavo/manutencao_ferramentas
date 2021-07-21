from django.urls import path
from .views import *


urlpatterns = [
    path('cliente/<int:id>', detail_cliente, name='detail_cliente'),
    path("clientes/", list_clintes, name='list_clintes'),
    path("cliente/add", create_cliente, name='create_cliente'),
]

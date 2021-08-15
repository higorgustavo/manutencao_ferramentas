from django.urls import path
from usuarios.views.pages_views import *

urlpatterns = [
    path("", dashboard, name='dashboad'),
    path("refresh", refresh_datas, name='refresh_datas'),
]

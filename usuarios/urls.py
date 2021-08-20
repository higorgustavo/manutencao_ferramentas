from django.urls import path
from usuarios.views.pages_views import *

urlpatterns = [
    path("", dashboard, name='dashboad'),
]

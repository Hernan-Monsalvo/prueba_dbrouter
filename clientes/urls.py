from . import views
from django.urls import path

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name="index")
]
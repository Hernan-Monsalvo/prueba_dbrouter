from . import views
from django.urls import path

app_name = 'informes'

urlpatterns = [
    path('', views.index, name="index")
]
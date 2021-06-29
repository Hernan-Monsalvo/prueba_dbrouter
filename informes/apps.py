from django.apps import AppConfig


class InformesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'informes'

class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
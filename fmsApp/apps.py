from django.apps import AppConfig


class FmsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fmsApp'

    def ready(self):
        import fmsApp.signals

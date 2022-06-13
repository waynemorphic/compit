from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

# connecting the signal module that bypasses the ready method
def ready(self):
    import core.signals
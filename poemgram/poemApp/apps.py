from django.apps import AppConfig
from django.db.models.signals import post_save

class PoemappConfig(AppConfig):
    name = 'poemApp'

    def ready(self):
        import poemApp.signals


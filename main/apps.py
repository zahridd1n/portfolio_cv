from django.apps import AppConfig
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        models = apps.get_models()
        for model in models:
            try:
                admin.site.register(model)
            except AlreadyRegistered:
                pass

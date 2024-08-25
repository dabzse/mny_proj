from django.apps import AppConfig


class DevelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "devel"

    def ready(self):
        import devel.templatetags.custom_tags
from django.apps import AppConfig


class DbEventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "db_events"

    def ready(self):
        import db_events.signals

"""MainConfig file."""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """New configurations for django."""

    default_auto_field = 'django.db.models.AutoField'
    name = 'main'

    def ready(self):
        """Parents func to init signals."""
        import main.signals  # noqa

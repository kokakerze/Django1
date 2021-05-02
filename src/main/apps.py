"""MainConfig file."""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Set MainConfig."""

    name = 'main'

    def ready(self):
        """Parents func to init signals."""
        import main.signals  # noqa

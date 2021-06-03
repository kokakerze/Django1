"""CELERY MODULE."""
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django1.settings')

app = Celery('Django1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


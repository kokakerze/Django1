"""Realise deferred functions."""
from datetime import datetime, timedelta

from celery import shared_task
from main.models import Logger, Subscriber
from main.services.notify_service import email_send
import requests


@shared_task
def notify_async(email_to, author_name):
    """Notifing asyncrones."""
    email_send(email_to, author_name)
    print("I have send_mail on notify_async - email_to:{}".format(email_to))


@shared_task
def delete_logs():
    """Delete logs from database."""
    Logger.objects.filter(created_lte=(datetime.now() - timedelta(days=3))).delete()


@shared_task
def mail_send_9am():
    """Send emails at 9am every morning."""
    from django.core.mail import send_mail
    result = requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')
    page = result.text
    emails = list(Subscriber.objects.values_list("email_to", flat=True))

    send_mail(
        "DesignBlog",
        page,
        "pavlovdesigh@gmail.com",
        emails,
        fail_silently=False
    )

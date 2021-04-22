"""Notifing after Subscribing."""
from django.http import request


def notify(email_to, author_name):
    """Notifying."""
    print("----- notify: {}".format(email_to))
    email_send(email_to, author_name)
    # telegram_notify(email_to)


def email_send(email_to, author_name):
    """Try write services."""
    from django.core.mail import send_mail

    send_mail(
        "DesignBlog",
        "You have subscribed on Author: {}".format(author_name),
        "pavlovdesigh@gmail.com",
        [email_to],
        fail_silently=False
    )


def telegram_notify(email_to):
    """Telegram notification."""
    Telegram()
    Telegram.notify(msg="Welcome")


class Telegram:
    """Class for notification by Telegram."""

    def notify(self, msg):
        """Params for notification."""
        telegram_url = 'https://api.telegram.org/bot<Token>'
        params = {"chat_id": "blablabla", "text": msg}
        response = request.POST(telegram_url + "sendMessage", data=params)
        return response

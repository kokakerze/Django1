"""Notifing after Subscribing."""
from django.http import request


def notify(email_to):
    """Notifying."""
    email_send(email_to)
    # telegram_notify(email_to)


def email_send(email_to):
    """Try write services."""
    pass


def telegram_notify(email_to):
    """Telegram notification."""
    Telegram()
    Telegram.notify("Welcome")


class Telegram:
    """Class for notification by Telegram."""

    def notify(self, msg):
        """Params for notification."""
        telegram_url = 'https://api.telegram.org/bot<Token>'
        params = {"chat_id": "blablabla", "text": msg}
        response = request.post(telegram_url + "sendMessage", data=params)
        return response

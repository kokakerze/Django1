"""Realise deferred functions."""
from account.models import User
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_activation_link_mail(user_id):
    """Send activation link to the registered user."""
    user = User.objects.get(id=user_id)
    link = settings.DOMAIN + "/activate/" + str(user.confirmation_token)
    msg = f"Activation link {link}"
    send_mail(
        "Super Space Blog: Activate your account",
        msg,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        # fail_silently=False,
    )

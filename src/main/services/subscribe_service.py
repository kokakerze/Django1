"""Subscribers service."""
from django.core.exceptions import ObjectDoesNotExist
from main.models import Author
from main.models import Subscriber


def subscribe(author_id, email_to):
    """Subscribe on author if not existing in Database."""
    try:
        Subscriber.objects.get(email_to=email_to, author_id=int(author_id))
        return False

    except ObjectDoesNotExist:
        author = Author.objects.get(id=author_id)
        subscriber = Subscriber(email_to=email_to, author_id=author)
        subscriber.save()
        return True

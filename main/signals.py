"""Signals module."""
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Author


@receiver(pre_save, sender=Author)
def author_pre_save(sender, instance, **kwargs):
    """Signal post saving in Author."""
    print('-----------pre_save')
    # breakpoint()
    instance.name = instance.name.lower() + "[name author7]"
    instance.email = instance.email + "[email author8]"


@receiver(post_save, sender=Author)
def author_post_save(sender, instance, created, **kwargs):
    """Signal post saving in Author."""
    print('===========post_save')
    # breakpoint()
    # instance.name = instance.name + "[name author]"
    if created:
        print("Created")
    else:
        print('Exist')

"""Create users models for project."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Save Superuser in models."""

    email = models.EmailField('email address', blank=False, null=False, unique=True)

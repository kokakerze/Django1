"""Create users models for project."""
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Save Superuser in models."""

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    email = models.EmailField('email address', blank=False, null=False, unique=True)
    confirmation_token = models.UUIDField(default=uuid.uuid4)

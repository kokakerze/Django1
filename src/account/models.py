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


def user_ava_upload(instance, filename):
    """Save in users id folder profile_picture."""
    return f'{instance.user_id}/{filename}'


class Avatar(models.Model):
    """Profile picture model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.ImageField(upload_to=user_ava_upload)


class Profile(models.Model):
    """Profile model as addition to each User."""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to=user_ava_upload)
    website_url = models.URLField(max_length=255, null=True, blank=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)
    twitter_url = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Return a string representation of user."""
        return str(self.user)

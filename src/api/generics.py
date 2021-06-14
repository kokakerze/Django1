"""This file include serializers for api mode."""

from main.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Create serializers."""

    class Meta:
        """Class Meta for post models."""

        model = Post
        fields = (
            'id',
            'title',
            'description',
            'content',
            'mood',
            'updated',
            'created',
            'get_mood_display'
        )

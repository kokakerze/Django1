"""This file include serializers for api mode."""

from rest_framework import serializers

from main.models import Book, Post, Author


class PostSerializer(serializers.ModelSerializer):
    """Create serializers for posts."""

    class Meta:
        """Class Meta for post serializers."""

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


class BookSerializer(serializers.ModelSerializer):
    """Create serializers for Books model."""

    class Meta:
        """Class Meta for book  serializers."""

        model = Book
        fields = (
            'id',
            'title',
            'author',
            'category',
        )


class AuthorSerializer(serializers.ModelSerializer):
    """Create serializers for Author model."""

    class Meta:
        """Class Meta for book  serializers."""

        model = Author
        fields = (
            'id',
            'name',
            'last_name',
            'email',
            'age',
        )

"""Filters for Search."""
import django_filters

from main.models import Book, Post


class PostFilter(django_filters.FilterSet):
    """Create Filter for PostsListView."""

    class Meta:
        """Class Meta for PostFilter."""

        model = Post
        fields = ['content', ]


class BookFilter(django_filters.FilterSet):
    """Create Filter for BooksListView."""

    class Meta:
        """Class Meta for BookFilter."""

        model = Book
        fields = ['title']

"""This is API View file."""

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.generics import BookSerializer, PostSerializer
from main.models import Book, Post


class PostAPIViewSet(viewsets.ModelViewSet):
    """SET API View for Post model."""

    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination


class BooksAPIViewSet(viewsets.ModelViewSet):
    """SET API View for Books model."""

    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

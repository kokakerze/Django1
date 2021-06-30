"""This is API View file."""
from api.generics import AuthorSerializer, BookSerializer, PostSerializer
from main.models import Author, Book, Post
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


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


class AuthorAPIViewSet(viewsets.ModelViewSet):
    """SET API View for Author model."""

    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    pagination_class = PageNumberPagination


class AuthorAPISet(generics.GenericAPIView):
    """Set API View for Author model version2."""

    queryset = Author.objects.all().order_by('-id')

    def get(self, request):
        """Get Author in api."""
        res = Author.objects.all().order_by('-id')
        ser = AuthorSerializer(res, many=True)
        return Response(ser.data)

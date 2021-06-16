"""This is API View file."""

from api.generics import PostSerializer
from main.models import Post
from rest_framework import viewsets


class PostAPIViewSet(viewsets.ModelViewSet):
    """SET API View."""

    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

"""This file sets API urls for website."""
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import AuthorAPISet

router = DefaultRouter()
router.register(prefix='posts', viewset=views.PostAPIViewSet, basename='post')
router.register(prefix='books', viewset=views.BooksAPIViewSet, basename='book')
router.register(prefix='author', viewset=views.AuthorAPIViewSet, basename='author')

urlpatterns = [
    path('authors/list/', AuthorAPISet.as_view(), name='api_authors_list'),
]

urlpatterns.extend(router.urls)

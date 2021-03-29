from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('posts/create', views.post_create, name='post_create'),
    path('api/posts', views.api_posts, name='api_posts'),
]

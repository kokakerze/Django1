"""This file sets urls for website."""
# from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('posts/create', views.post_create, name='post_create'),
    path('posts/subcribe', views.posts_subscribe, name='posts_subscribe'),

    path('api/posts', views.api_posts, name='api_posts'),
    path('api/subcribe', views.api_subscribe, name='api_subscribe'),
]

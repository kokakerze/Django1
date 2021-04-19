"""This file sets urls for website."""
# from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [

    path('', TemplateView.as_view(template_name='main/index.html'), name='homepage'),
    path('about/', views.about, name='about'),

    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update/<int:post_id>/', views.post_update, name='post_update'),
    path('posts/', views.posts_all, name='posts_all'),
    path('posts/<int:post_id>/', views.post_show, name='post_show'),

    path('subcribers/new/', views.subscribers_new, name='subscribers_new'),
    path('subcribers/all/', views.subscribers_all, name='subscribers_all'),
    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/all/', views.authors_all, name='authors_all'),


    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/subcribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/new/', views.api_authors_new, name='api_authors_new'),
]

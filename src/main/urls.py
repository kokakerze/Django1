"""This file sets urls for website."""
# from django.contrib import admin
# from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from django.views.decorators import cache
from django.views.generic import TemplateView
from Django1 import settings

from . import views

urlpatterns = [

    path('', TemplateView.as_view(template_name='main/index.html'), name='homepage'),
    path('about/', views.about, name='about'),

    path('posts/create/', views.post_create, name='post_create'),
    path('posts/update/<int:post_id>/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('posts/', views.posts_all, name='posts_all'),
    path('posts/all/', cache.cache_page(120)(views.PostsListView.as_view()), name='posts_list'),
    path('posts/list/csv', views.PostCSVView.as_view(), name='posts_list_csv'),
    path('posts/list/xls', views.PostXLSView.as_view(), name='posts_list_xls'),
    path('posts/<int:post_id>/', views.post_show, name='post_show'),

    path('subcribers/new/', views.subscribers_new, name='subscribers_new'),
    path('subcribers/all/', views.subscribers_all, name='subscribers_all'),
    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/<int:pk>/delete/', views.DeleteAuthorsView.as_view(), name='author_delete'),
    path('authors/all/', views.AuthorsListView.as_view(), name='authors_all'),
    path('authors/list/', views.AuthorsList2View.as_view(), name='authors_list'),
    path('books/all/', views.BookListView.as_view(), name='books_all'),
    path('category/all/', cache.cache_page(600)(views.category_all), name='category_all'),


    path('api/v1/', include('api.urls')),

    path('contact-us/create/', views.ContactUsView.as_view(), name='contact-us-create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

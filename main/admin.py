"""File registering models."""
from django.contrib import admin
from main.models import Author, Post, Subscriber

# Register your models here.


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)

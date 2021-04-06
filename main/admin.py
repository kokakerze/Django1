"""File registering models."""
from django.contrib import admin
from main.models import Post, Author, Subscriber

# Register your models here.


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)

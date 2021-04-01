"""File registering models."""
from django.contrib import admin
from main.models import Post, User
# Register your models here.


admin.site.register(User)
admin.site.register(Post)

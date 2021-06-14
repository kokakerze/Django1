"""File registering models."""
from account.models import Avatar, User, Profile
from django.contrib import admin

from .models import Author, Comments, Logger, Post, Subscriber


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    """Sort comments in admin view."""

    list_display = ("subs_id", "body", "post", "created", "activate")
    list_filter = ("activate", "created", "updated")
    search_fields = ("subs_id", "body")


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscriber)
admin.site.register(Logger)
admin.site.register(Comments, CommentAdmin)
admin.site.register(User)
admin.site.register(Avatar)
admin.site.register(Profile)

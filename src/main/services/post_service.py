"""Show all posts method."""
import datetime

from django.core.cache import cache

from src.main.forms import CommentsForm
from src.main.models import Post


def postall():
    """Take all objects from Post class."""
    key = Post().__class__.cache_key()
    if key in cache:
        objects_all = cache.get(key)
    else:
        objects_all = Post.objects.all()
        cache.set(key,objects_all,30)
    return objects_all


def post_find(post_id: int) -> Post:
    """Find recent post."""
    return Post.objects.get(id=post_id)


def comment_method(post, request):
    """Show comments and realise new comments."""
    comments = post.comments.filter(activate=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentsForm()
    return comment_form, comments

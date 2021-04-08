"""Show all posts method."""
from main.models import Post


def postall():
    """Take all objects from Post class."""
    objects_all = Post.objects.all()
    return objects_all


def post_find(post_id: int) -> Post:
    """Find recent post."""
    return Post.objects.get(id=post_id)

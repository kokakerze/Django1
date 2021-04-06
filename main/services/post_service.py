from main.models import Post


def postall():
    """Takes all objects from Post class."""
    objects_all = Post.objects.all()
    return objects_all
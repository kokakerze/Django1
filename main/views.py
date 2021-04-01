"""ViewsFile that manages information that shows in urls."""

from django.http import JsonResponse
from django.shortcuts import render
from main.forms import PostForm
from main.models import Post


def index(request):
    """Show main page."""
    return render(request, "main/index.html")


def about(request):
    """Show about page."""
    return render(request, "main/about.html", {"title": "About Company"})


def posts(request):
    """Show posts page."""
    posts = Post.objects.all()
    return render(request, "main/posts.html", {'title': "Posts", "posts": posts})


def post_create(request):
    """Show create Post page."""
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = "Cannot save the post"
    else:
        form = PostForm()
        context = {"form": form, "errors": errors}
    return render(request, "main/post_create.html", context=context)


def api_posts(request):
    """Show posts in Json format."""
    posts = Post.objects.all()
    responseData = [dict(title=post.title, description=post.description, content=post.content) for post in posts]
    return JsonResponse(responseData, safe=False)

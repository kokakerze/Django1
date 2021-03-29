import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from main.models import Post
from main.forms import PostForm


def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html",{"title": "About Company"})

def posts(request):
    posts = Post.objects.all()
    return render(request,"main/posts.html",{'title': "Posts","posts":posts})


def post_create(request):
     errors=''
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             form.save()
         else:
            errors = "Cannot save the post"
     else:
         form = PostForm()
     context = {
         "form": form,
         "errors": errors
     }
     return render(request, "main/post_create.html", context=context)

def api_posts(request):
    posts = Post.objects.all()
    responseData = [dict(title=post.title, description=post.description, content=post.content) for post in posts]
    return JsonResponse(responseData, safe=False)


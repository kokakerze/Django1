"""ViewsFile that manages information that shows in urls."""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from faker import Faker
from main.forms import PostForm, SubscriberForm
from main.models import Author, Post, Subscriber
from main.services.notify_service import notify
from main.services.post_service import post_find, postall
from main.services.subscribe_service import subscribe


def index(request):
    """Show main page."""
    return render(request, "main/index.html")


def about(request):
    """Show about page."""
    return render(request, "main/about.html", {"title": "About Company"})


def posts_all(request):
    """Show posts page."""
    return render(request, "main/posts_all.html", {'title': "Posts", "posts": postall()})


def post_create(request):
    """Show create Post page."""
    errors = ''
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_all")
        else:
            errors = "Не возможно сохранить пост."
    else:
        form = PostForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/post_create.html", context=context)


def subscribers_new(request):
    """Subscribe on Post bi ID authors."""
    # Получить автора
    # Подписаться под автором
    errors = ''
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subscribers_all")
            # author_id = request.POST['author_id']
            # email_to = request.POST['email_to']
            # subscribe_success = subscribe_notify(author_id, email_to)
            # if subscribe_success:
            #     return redirect("posts")
            # else:
            #     errors = "Вы уже подписаны на этого автора."
        else:
            errors = form.errors
    else:
        form = SubscriberForm()
    context = {"form": form, "errors": errors}
    return render(request, "main/subscribers_new.html", context=context)


def subscribe_notify(author_id, email_to):
    """Subscribe and notifing process."""
    # if subscribe(author_id, email_to):
    #     notify(email_to)
    #     return True
    # return False
    subscribe(author_id, email_to)
    notify(email_to)


def subscribers_all(request):
    """Show all subscribers."""
    allsubs = Subscriber.objects.all()
    return render(request, "main/subscribers_all.html", {"title": "Все подписки", "subscribers_all": allsubs})


def authors_new(request):
    """Generate fake author by Faker."""
    fake = Faker()
    Author(name=fake.name(), email=fake.email()).save()
    return redirect("authors_all")


def authors_all(request):
    """Show a list of authors."""
    allauthors = Author.objects.all()
    return render(request, "main/authors_all.html", {"title": "Авторы", "authors": allauthors})


def post_update(request, post_id):
    """Update recent posts."""
    err = ""
    pst = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_all")
        else:
            err = "Не возможно обновить пост."
    else:
        form = PostForm(instance=pst)
    context = {
        "form": form,
        "err": err
    }
    return render(request, "main/post_update.html", context=context)


def post_show(request, post_id):
    """Show post by ID."""
    pst = post_find(post_id)
    return render(request, "main/post_show.html", {"title": pst.title, "pst": pst})


def api_authors_new(request):
    """Generate fake author by Faker for API in Json Format."""
    fake = Faker()
    Author(name=fake.name(), email=fake.email()).save()
    authors = Author.objects.all().values("name", "email")
    return JsonResponse(list(authors), safe=False)


def api_posts(request):
    """Show posts in Json format."""
    posts = postall()
    responded = [dict(title=post.title, description=post.description, content=post.content) for post in posts]
    return JsonResponse(responded, safe=False)


def api_subscribe(request):
    """Show subcribers of authors."""
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to "]
    get_object_or_404(Author, pk=author_id)
    subscribe_notify(author_id, email_to)
    data = {"author_id": author_id}
    return JsonResponse(data, safe=False)

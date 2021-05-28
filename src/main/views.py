"""ViewsFile that manages information that shows in urls."""
import csv

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View
from faker import Faker
from main.forms import PostForm, SubscriberForm
from main.models import Author, Book, Category, ContactUs, Post, Subscriber
from main.services.notify_service import notify
from main.services.post_service import comment_method, post_find, postall
from main.services.subscribe_service import subscribe
from main.tasks import notify_async
from prompt_toolkit.validation import ValidationError
import xlwt


def index(request):
    """Show main page."""
    return render(request, "main/index.html")


def about(request):
    """Show about best page."""
    return render(request, "main/about.html", {"title": "About Company"})


def posts_all(request):
    """Show posts page."""
    context = {'title': "Posts", "posts": postall()}
    return render(request, "main/posts_all.html", context)


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
    errors = ''
    subscribe_success = False

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                subscribe_success = True
            else:
                errors = form.errors
        except ValidationError:
            errors = "Already subscribed."
    else:
        form = SubscriberForm()
    if subscribe_success:
        delayed_notify(request)
        return redirect("subscribers_all")
    context = {"form": form, "errors": errors}
    return render(request, "main/subscribers_new.html", context=context)


def delayed_notify(request):
    """Notifies subscribers in delayed tasks."""
    email_to = request.POST.get('email_to')
    author_id = request.POST.get('author_id')
    author = Author.objects.get(id=author_id)
    notify_async.delay(email_to, author.name)


def subscribe_notify(author_id, email_to, authors_name):
    """Subscribe and notifying process."""
    subscribe(author_id, email_to)
    notify(email_to, authors_name)


def subscribers_all(request):
    """Show all subscribers."""
    allsubs = Subscriber.objects.all()
    return render(request, "main/subscribers_all.html", {"title": "Все подписки", "subscribers_all": allsubs})


def authors_new(request):
    """Generate fake author by Faker."""
    fake = Faker()
    Author(name=fake.name(), email=fake.email()).save()
    return redirect("authors_all")


# def authors_all(request):
#     """Show a list of authors."""
#     allauthors = Author.objects.all().prefetch_related("books")
#     context = {"title": "Авторы", "authors": allauthors}
#     return render(request, "main/authors_all.html", context)


def books_all(request):
    """Show a list of authors."""
    # books = Book.objects.all().select_related("author")
    books = Book.objects.all().only("id", "title", "author__last_name", "category").select_related("author")
    context = {"title": "Книги", "books": books}
    return render(request, "main/books_all.html", context)


def category_all(request):
    """Show a list of authors."""
    # cat = Category.objects.all()
    cat = Category.objects.all().prefetch_related("books_cat")
    context = {"title": "Категории", "categories": cat}
    return render(request, "main/categories_all.html", context)


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
    """Show post by ID+ comments."""
    pst = post_find(post_id)
    comment_form, comments = comment_method(pst, request)
    return render(request, "main/post_show.html",
                  {"title": pst.title, "pst": pst, "comments": comments, "comment_form": comment_form})


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
    """Show subscribers of authors."""
    author_id = request.POST.get('author_id')
    author = Author.objects.get(id=author_id)
    email_to = request.GET["email_to "]
    get_object_or_404(Author, pk=author_id)
    subscribe_notify(authors_name=author.name, email_to=email_to, author_id=author_id)
    data = {"author_id": author_id}
    return JsonResponse(data, safe=False)


class PostsListView(ListView):
    """Show list of posts analogously."""

    # queryset = Post.objects.all()

    def get_queryset(self):
        """Set queryset to listview."""
        queryset = Post.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Set context data for ListView."""
        context = super().get_context_data(*args, **kwargs)
        context["cnt"] = context['object_list'].count()
        context["title"] = "Все посты"
        return context


class ContactUsView(CreateView):
    """Create contact us Form as view."""

    success_url = reverse_lazy("homepage")
    model = ContactUs
    fields = ("email", "subject", "msg")


def display_attribute(obj, attrs: str):
    """Check of Nonviable attributes and show all attributes."""
    get_display = f"get_{attrs}_display"
    if hasattr(obj, get_display):
        return getattr(obj, get_display)()
    return getattr(obj, attrs)


class PostCSVView(View):
    """Download Posts in CSV format."""

    headers = ["title", "description", "mood"]

    def get(self, request, *args, **kwargs):
        """Download list of posts in CSV."""
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type='text/csv',
            # headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(self.headers)
        for post in Post.objects.all().iterator():
            # for header in headers:
            #     if hasattr(post, f"get_{header}_display"):
            row = [display_attribute(post, header) for header in self.headers]
            writer.writerow(row)

        return response


class PostXLSView(View):
    """Download Posts in XLS format."""

    def get(self, request, *args, **kwargs):
        """Download list of posts in CSV."""
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(
            content_type='application/ms-excel'
            # headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        response['Content-Disposition'] = 'attachment; filename="PostsFromCleanBlog.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("sheet1")
        row_num = 0
        columns = ["title", "content", "mood"]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()
        data = Post.objects.all()
        for post in data:
            row_num = row_num + 1
            ws.write(row_num, 0, post.title, font_style)
            ws.write(row_num, 1, post.content, font_style)
            ws.write(row_num, 2, post.mood, font_style)

        wb.save(response)
        return response


class AuthorsListView(ListView):
    """Show list of posts analogously."""

    def get_queryset(self):
        """Set queryset to listview."""
        key = Author().__class__.cache_key()
        if key in cache:
            queryset = cache.get(key)
        else:
            queryset = Author.objects.all().prefetch_related("books")
            cache.set(key, queryset, 60)
        return queryset


class DeletePostView(DeleteView):
    """Delete posts."""

    model = Post
    template_name = "main/post_delete.html"
    success_url = reverse_lazy("posts_list")


class DeleteAuthorsView(DeleteView):
    """Delete Authors."""

    model = Author
    template_name = "main/author_delete.html"
    success_url = reverse_lazy("authors_all")

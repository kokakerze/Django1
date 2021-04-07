"""Create models of Users and Posts in project."""
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    """Create models of Users."""

    class Meta:
        """Special class to define database and name's printing."""

        db_table = "tb_users"
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"
    name = models.CharField("Имя автора", max_length=90)
    email = models.EmailField("Почта автора", max_length=80)
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Set method of printing."""
        return self.name


class Subscriber(models.Model):
    """Create model of Subscriber."""

    class Meta:
        """Special class to define database and name's printing in admin."""

        db_table = "tb_subscribers"
        verbose_name_plural = "Подписчики"
        verbose_name = "Подписчик"
    # name = models.CharField("Имя подписчика", max_length=90)
    email_to = models.EmailField("Почта подписчика", max_length=80)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Set method of printing."""
        return self.email_to


class Post(models.Model):
    """Create model of Posts."""

    class Meta:
        """Special Meta class to define database and post names printing."""

        db_table = "tb_posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    """Setup title, description, content and dates of posts."""
    title = models.CharField("Заголовок поста", max_length=70)
    description = models.TextField("Описание поста", max_length=90)
    content = models.TextField("Контент поста")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        """Set method of printing."""
        return self.title

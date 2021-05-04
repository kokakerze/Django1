"""Create models of Users and Posts in project."""
from datetime import datetime

from django.core.cache import cache
from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    """Create models of Users."""

    class Meta:
        """Special class to define database and name's printing."""

        db_table = "tb_users"
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"

    name = models.CharField("Имя автора", max_length=90)
    last_name = models.CharField("Фамилия автора", max_length=90, blank=True)
    email = models.EmailField("Почта автора", max_length=80)
    age = models.IntegerField(default=0)
    """Setup name and email fields types and lengths."""

    def __str__(self):
        """Set method of printing."""
        return self.name

    def get_full_name(self):
        """Get full name from Authors."""
        return f'{self.name} {self.last_name}'

    @property
    def full_name(self):
        """Property of printing full name."""
        return f'{self.name} {self.last_name}'

    # def save(self, *args, **kwargs):
    #     print("Author before save.")
    #     self.name = self.name.lower()
    #     self.email = self.email
    #     super().save(*args, **kwargs)
    #     print("Author after save")


class Subscriber(models.Model):
    """Create model of Subscriber."""

    class Meta:
        """Special class to define database and name's printing in admin."""

        unique_together = ['email_to', 'author_id']
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

    MOOD_CHOICES = (
        (1, 'advertisments'),
        (2, 'news'),
        (3, 'weather'),
        (4, 'business'),
        (5, 'info'),
    )
    """Setup title, description, content and dates of posts."""
    title = models.CharField("Заголовок поста", max_length=70)
    description = models.TextField("Описание поста", max_length=90)
    content = models.TextField("Контент поста")
    mood = models.PositiveSmallIntegerField(choices=MOOD_CHOICES, default=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        """Set method of printing."""
        return self.title

    def save(self, **kwargs):
        super().save()
        key = self.__class__.cache_key()
        cache.delete(key)

    @classmethod
    def cache_key(cls):
        dt = datetime.today().strftime('%y-%m-%d')
        key = f'{dt}'
        return key


class Logger(models.Model):
    """Set Logger to website."""

    class Meta:
        """Special Meta class to define database."""

        db_table = "tb_loggers"

    utm = models.CharField("UTM метка", max_length=50)
    time_execution = models.CharField("Время выполнения", max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField("Path", max_length=70)
    user_ip = models.CharField("IP адрес пользователя", max_length=20)

    def __str__(self):
        """Set method of printing."""
        return self.utm


class Comments(models.Model):
    """Set comments model in database."""

    class Meta:
        """Special Meta class to define database and post ordering by created."""

        db_table = "tb_comments"
        ordering = ("created",)

    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    body = models.TextField("Комментариий")
    subs_id = models.ForeignKey("Subscriber", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)
    activate = models.BooleanField(default=True)

    def __str__(self):
        """Set method of printing."""
        return "Comment by {} on {}".format(self.subs_id, self.post)


class Book(models.Model):
    """Create a books for authors."""

    title = models.CharField("Название книги", max_length=250)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books_cat")


class Category(models.Model):
    """Set category for books."""

    category = models.CharField("Категория книги", max_length=40)


class ContactUs(models.Model):
    """Set contact us model."""

    email = models.EmailField()
    subject = models.CharField(max_length=120)
    msg = models.TextField()

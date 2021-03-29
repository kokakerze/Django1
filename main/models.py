from django.db import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = "tb_users"
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
    name = models.CharField("Имя пользователя",max_length=90)
    email = models.EmailField("Почта",max_length=80)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = "  tb_posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    title = models.CharField("Заголовок поста",max_length=70)
    description = models.TextField("Описание поста",max_length=90)
    content = models.TextField("Контент поста")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title




"""Generate random Authors and books for them."""

from faker import Faker
import random

from main.models import Author, Category
from main.models import Book

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """Generate random data."""
    help = "generate random data"

    def handle(self, *args, **options):
        Author.objects.all().delete()
        Category.objects.all().delete()
        fake = Faker()
        for _ in range(100):
            try:
                Author(name=fake.name(), email=fake.email(), age=random.randint(1, 100)).save()
                Category(category=fake.text(10)).save()
            except IntegrityError:
                pass
        for i in range(100):
            author = Author.objects.order_by("?").last()
            category = Category.objects.order_by("?").last()
            Book(title=f"Title {i}", author=author, category=category).save()

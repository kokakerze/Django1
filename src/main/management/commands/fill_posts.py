"""Parse command for post from another blog."""

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from main.models import Post
import requests


class Command(BaseCommand):
    """Parse random posts from url given."""

    url = "https://doroshenkoaa.ru/med/"

    def handle(self, *args, **options):
        """Parse posts from url."""
        Post.objects.all().delete()
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        link_list = []
        for link in soup.findAll("a", {"class": "more"}):
            link_list.append(link.get('href'))
        for link in link_list:
            r = requests.get(link)
            soup = BeautifulSoup(r.text, "html.parser")
            for c in soup.findAll("div", {"itemprop": "articleBody"}):
                content = c.text
            for t in soup.findAll("h1", {"itemprop": "headline"}):
                title = t.text.strip()
            Post.objects.create(title=title, content=content)

import random
from unittest import TestCase

import pytest
from django.test import Client, SimpleTestCase
from django.urls import reverse

from src.main.models import ContactUs, Post, Subscriber, Author


def test_contact_us_show(client):
    response = client.get(reverse("contact-us-create"))
    assert response.status_code == 200


def test_contact_us_post_empty(client):
    response = client.post(reverse("contact-us-create"))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Обязательное поле.'],
        'subject': ['Обязательное поле.'],
        'msg': ['Обязательное поле.']
    }


def test_contact_us_wrong_email(client):
    response = client.post(reverse("contact-us-create"), data={
        'email': 'no_valid_email',

    })
    assert response.context_data['form'].errors == {
        'email': ['Введите правильный адрес электронной почты.'],
        'subject': ['Обязательное поле.'],
        'msg': ['Обязательное поле.']
    }
    assert response.status_code == 200


def test_contact_us_correct_form_check_count(client):
    count_before = ContactUs.objects.count()
    response = client.post(reverse("contact-us-create"), data={
        'email': 'test@example.com',
        'subject': 'test',
        'msg': 'test',

    })
    assert response.status_code == 302
    assert ContactUs.objects.count() == count_before + 1

    response = client.post(reverse("contact-us-create"), data={
        'email': 'test@example.com',
        'subject': 'test',
        'msg': 'test',

    })

    assert response.status_code == 302
    assert ContactUs.objects.count() == count_before + 1


def test_contact_us_correct_form_check_count(client, fake_fixture):
    count_before = ContactUs.objects.count()
    response = client.post(reverse("contact-us-create"), data={
        'email': fake_fixture.email(),
        'subject': fake_fixture.word(),
        'msg': fake_fixture.word(),

    })
    assert response.status_code == 302
    assert ContactUs.objects.count() == count_before + 1


def test_authors(author_fixt):
    name = author_fixt.get_full_name()
    assert name is not None


def test_post_correct_form_check_count(client, fake_fixture):
    count_before = Post.objects.count()
    response = client.post(reverse("post_create"), data={
        'title': fake_fixture.word(),
        'description': fake_fixture.word(),
        'content': fake_fixture.word(),

    })
    assert response.status_code == 302
    assert Post.objects.count() == count_before + 1


class TestHomepage(SimpleTestCase):
    databases = '__all__'

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, 'Main Page')


class TestAbout(SimpleTestCase):
    databases = '__all__'

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, 'About')


def test_subscribers_new(client):
    response = client.get(reverse("subscribers_new"))
    assert response.status_code == 200


def test_subscribers_all(client):
    response = client.get(reverse("subscribers_all"))
    assert response.status_code == 200


def test_books_all(client):
    response = client.get(reverse("books_all"))
    assert response.status_code == 200

def test_post_all(client):
    response = client.get(reverse("posts_all"))
    assert response.status_code == 200


def test_category_all(client):
    response = client.get(reverse("category_all"))
    assert response.status_code == 200


def test_authors_new(client):
    before = Author.objects.count()
    response = client.get(reverse("authors_new"))
    assert response.status_code == 302
    assert Author.objects.count() == before + 1

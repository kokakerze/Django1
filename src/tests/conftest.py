import pytest

from faker import Faker

from src.account.models import User
from src.main.models import Author, Post, Subscriber
from random import randint


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope='function')
def acc_fixt():
    acc = User.objects.create()
    yield acc


@pytest.fixture(scope='function')
def author_fixt():
    auth = Author.objects.create()
    yield auth


@pytest.fixture(scope='function')
def post_fixt():
    posts = Post.objects.create()
    yield posts


@pytest.fixture(scope='function')
def fake_fixture():
    faker = Faker()
    yield faker




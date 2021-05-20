
import pytest
from django.urls import reverse


@pytest.mark.skip(reason="skipitnow")
def test_skip():
    pass


@pytest.mark.xfail(reason="wrong math", struct=True)
def test_fail():
    assert 200 == 201


@pytest.mark.xfail(reason=(AssertionError, TimeoutError))
def test_fail2():
    raise AssertionError


# def test_homepage(client):
#     response = client.get(reverse("homepage"))
#     breakpoint()
#     assert 200 == 201

def test_with_client(client):
    response = client.get('/')
    breakpoint()
    assert 200 == 201
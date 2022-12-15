import pytest


@pytest.fixture
def setup():
    print("LAunch Browser")
    print("Load URL")
    print("Brwose product")
    yield
    print("Close Browser")

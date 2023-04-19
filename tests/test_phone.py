import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone):
    assert phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    assert phone.__str__() == 'iPhone 14'

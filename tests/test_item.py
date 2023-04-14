"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 100000


def test_discount(item):
    item.apply_discount()
    assert item.price == 20000


def test_string_to_number(item):
    assert item.string_to_number('5') == 5
    assert item.string_to_number('5.5') == 5
    assert item.string_to_number('5.0') == 5


def test_instantiate_from_csv(item):
    assert item.instantiate_from_csv() is None

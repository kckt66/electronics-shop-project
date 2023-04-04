"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def number():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(number):
    assert number.calculate_total_price() == 100000


def test_discount(number):
    number.apply_discount()
    assert number.price == 20000

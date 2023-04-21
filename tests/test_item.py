"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


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


def test_repr(item):
    assert item.__repr__() == "Item('Ноутбук', 20000, 5)"


def test_str(item):
    assert item.__str__() == 'Ноутбук'


def test_add(item, phone):
    assert item + phone == 10
    assert phone + phone == 10

    with pytest.raises(Exception):
        item + 10


def test_name_setter(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


    with pytest.raises(ValueError):
        item.name = 'СуперНоутбук'


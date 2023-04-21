import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone):
    assert phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    assert phone.__str__() == 'iPhone 14'


def test_sim_setter(phone):
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2



    with pytest.raises(ValueError):
        phone.number_of_sim = 0

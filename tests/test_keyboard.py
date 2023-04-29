import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_language():
    assert kb.language == 'EN'

    kb.change_lang()
    assert kb.language == 'RU'

    kb.change_lang().change_lang()
    assert kb.language == 'RU'

    with pytest.raises(AttributeError):
        kb.language = 'CH'

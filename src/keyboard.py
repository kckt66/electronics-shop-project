from src.item import Item
from src.MixinLang import MixinLang


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity, language='EN'):
        """
        Создание экземпляра класса kb.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Язык раскладки на клавиатуре.
        """
        super().__init__(name, price, quantity)
        self.language = language


    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, lang):

        if lang not in ['EN', 'RU']:
            raise AttributeError("AttributeError: property 'language' of 'KeyBoard' object has no setter")
        self._language = lang

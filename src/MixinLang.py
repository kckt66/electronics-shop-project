

class MixinLang:
    """Класс-миксин для изменения языка в классе Keyboard"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_lang = self.language
        self.language = 'RU'


    def change_lang(self):
        if self.language == 'RU':
            self.language = 'EN'
        else:
            self.language = 'RU'
        return self

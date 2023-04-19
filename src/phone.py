from src.item import Item


class Phone(Item):


    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество симкарт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_sim(self):
        return self.number_of_sim

    @number_sim.setter
    def number_sim(self, number_of_sim):
        self.number_of_sim = number_of_sim
        if self.number_of_sim < 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError


    def __str__(self):
        return f'{self.name}'


    def __repr__(self):
        return f"{self.__class__.__name__}{(self.name, self.price, self.quantity, self.number_of_sim)}"

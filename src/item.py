import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.__name}'


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.name) <= 10:
            self.__name = name
        else:
            raise ValueError('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity

        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate



    @classmethod
    def instantiate_from_csv(cls, file_name="../src/items.csv"):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        try:
            with open(file_name, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('FileNotFoundError: Отсутствует файл item.csv')
        except KeyError:
            raise InstantiateCSVError('InstantiateCSVError: Файл item.csv поврежден')




    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        i = string[0]
        return int(i)


    def __add__(self, other):
        """
        Сложение экземпляром родительского класса и дочернего
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

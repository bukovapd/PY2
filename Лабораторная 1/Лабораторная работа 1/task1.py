# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Bilding:
    """
    Класс описывает здание.
    """
    def __init__(self, floor: int, material: str):
         """ Инициализация экземпляра класса.
         :param floor: количество этажей в здании
         :param material: материал, из которого построено здание
         """
         if floor > 15:
             raise ValueError("Очень высокий дом")
         if floor < 3:
             raise ValueError("Очень низкий дом")
         self.floor = floor
         self.material = material

    def name_of_material(self) -> str:
        """
        Метод для обозначения материала.

        :return возвращает название материала, из которого построен дом
        """
        pass

    def amount_of_material(self, material_tons: int) -> int:
        """
        Метод для обозначения количества материала, необходимого для постройки дома.
        :param material_tons: количества материала в тоннах
        :return: возвращает переменную с типом int
        """
        pass


class Book:
    """
    Класс описывает модель книги.
    """

    def __init__(self, amount_of_pages: int, gerne_of_book: str):
        """ Инициализация экземпляра класса.
         :param amount_of_pages: количество страниц
         :param gerne_of_book: жарн книги
         """
        if amount_of_pages > 400:
            raise ValueError("Большая книга")
        if amount_of_pages < 100:
            raise ValueError("Маленькая книга")
        self.amount_of_pages = amount_of_pages
        self.gerne_of_book = gerne_of_book

    def amount_of_reviews(self, amount: int) -> int:
        """
        Метод для обозначения количества отзывов о книге
        :param amount: обозначает количесво отзывов на книгу
        :return: возвращает переменную с типом int
        """

        pass

    def exam(self, chapter_of_book: int) -> int:
        """
        Метод для обозначения номера главы
        :param chapter_of_book: обозначение кол-ва главы
        :return: возвращает переменную с типом int
        """
        pass




class Donut:
    """
    Класс описывает модель заказа пончиков.
    """

    def __init__(self, color_of_donut: str, amount_of_donuts: int):
        """ Инициализация экземпляра класса.
        :param science: предметная область учебника
        :param pages: кол-во страниц учебника
        """
        self.color_of_donut = color_of_donut
        self.amount_of_donuts = amount_of_donuts
        if amount_of_donuts > 50:
            raise ValueError("Недопустимое кол-во для заказа")
        if amount_of_donuts < 5:
            raise ValueError("Недопустимое кол-во для заказа")

    def color_donut(self) -> str:
        """
        Метод для обозначения цвета пончика.
        :return: возвращает название цвета пончика
        """
        pass



# TODO работоспособность экземпляров класса проверить с помощью doctest

if __name__ == "__main__":

    doctest.testmod()
    pass

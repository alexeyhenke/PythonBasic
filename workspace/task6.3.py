"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
   Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
   оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.

   В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
   Проверить работу примера на реальных данных (создать экземпляры класса Position,
   передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы Worker (работник)"))
print("= " * 50)


class Worker:
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print(f'{self._income.values()}')

   # @property
    def income(self):
        return float(self._income["wage"] + self._income["bonus"])


# __end_class_Worker__

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        print(f'Новый сотрудник {self.name} {self.surname}')

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        # print(f'${str(super().income)}')
        return super().income


# __end_class_Position__

big_boss = Position("Иван", "Иванов", "Директор", 100000, 100000)
print(f'Он имеет позицию {big_boss.position} в нашей фирме')
print(f'Наш {big_boss.position} имеет З/П ${big_boss.get_total_income()}')
print("- " * 10)
groundsman = Position('Андрей', 'Пупкин', 'Землекоп', 10000, 90000)
print(f'Наш {groundsman.position} имеет З/П ${groundsman.get_total_income()}')

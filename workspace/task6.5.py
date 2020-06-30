"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
   Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
   В каждом из классов реализовать переопределение метода draw.
   Для каждого из классов методы должен выводить уникальное сообщение.
   Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы 'Канцелярка'! "))
print("= " * 50)


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


# __end_class_Stationery__

class Pen(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color
        print(f'Создали ручку: чернила имееют {self.color} цвет')

    def draw(self):
        print(f'Ручка пишет: она имеет {self.color} цвет')


# __end_class_Pen__

class Pencil(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color
        print(f'Создали карандаш: цвет {self.color}')

    def draw(self):
        print(f'{self.color} карандаш рисует')


# __end_class_Pencil__

class Handle(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color
        print(f'Создали маркер: цвет {self.color}')

    def draw(self):
        print(f'{self.color} маркер рисует')


# __end_class_Handle__

black_pen = Pen("Белая ручка", "черный")
print(f'{black_pen.title}')
print("- " * 10)
blue_pen = Pen("Черная ручка", "синий")
print(f'{blue_pen.title}')
print("- " * 10)

black_pen.draw()
print(f'Начинаем рисовать используя {blue_pen.title} она имеет {blue_pen.color} цвет')

print("- " * 10)
red_pencil = Pencil("Красный карандаш", "красный")
red_pencil.draw()

print("- " * 10)
green_marker = Handle("Зеленый маркер", "зеленый")
green_marker.draw()

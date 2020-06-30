"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
   Значения данных атрибутов должны передаваться при создании экземпляра класса.
   Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
   Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
   толщиной в 1 см * число см толщины полотна. Проверить работу метода.

   Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы расчета Road (дорога)!"))
print("= " * 50)


class Road:
    ASPHALT_MASS = 25

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def mass_calculation(self, deep: float):
        return ((self._length * self._width * self.ASPHALT_MASS) * deep) / 1000


# __end_class_road__

length_float = 5000
width_float = 20
deep_float = 5

road = Road(length_float, width_float)
print(f'Масса асфальта для дороги протяженностью в {length_float} метров, '
      f'составит: {str(road.mass_calculation(deep_float))} тонн.')

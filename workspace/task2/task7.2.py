"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
   К типам одежды в этом проекте относятся пальто и костюм.
   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
   Это могут быть обычные числа: V и H, соответственно.

   Для определения расхода ткани по каждому типу одежды использовать формулы:
        для пальто (V/6.5 + 0.5),
        для костюма (2 * H + 0.3).
    Проверить работу этих методов на реальных данных.

   Реализовать общий подсчет расхода ткани.
   Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
   проверить на практике работу декоратора @property
"""

from workspace.task2.Сoat import Coat
from workspace.task2.Suit import Suit

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в программу расчета расхода ткани на производство одежды!"))
print("= " * 50)


size_dict = {"XS": 42, "S": 46, "M": 48, "L": 50, "XL": 52, "XXL": 54}
growth_dict = {"XS": 1, "S": 1, "M": 2, "L": 3, "XL": 4, "XXL": 5}

men_black_coat = Coat("Classic Coat", "Men's", size_dict["XXL"])
men_brown_coat = Coat("Classic Coat", "Men's", size_dict["XL"])
women_pink_coat = Coat("Short Coat", "Women", size_dict["S"])

material_spent = men_brown_coat.cloth_spent(men_brown_coat.coat_size)
print("- " * 20)
print(f'Пальто мужское: {men_brown_coat.get_clothe_type} имеет размер {men_brown_coat.coat_size}')
print(f'На пошив этого пальто потребовалось {material_spent} метров сукна')

print("- " * 20)
material_spent = men_black_coat.cloth_spent(men_black_coat.coat_size)
print(f'На пошив черного пальто потребовалось {material_spent} метров сукна')

print("- " * 20)
women_black_suit = Suit("Classic suit", "women", size_dict["S"])
print(f'Костюм черного цвета {women_black_suit.get_clothe_type} {women_black_suit.suit_size} размера')
print(f'На пошив черного костюма потребовалось {women_black_suit.cloth_spent(growth_dict["S"])} метров сукна')
"""
   Класс Пальто
"""
from workspace.task2.AbstractClothes import AbstractClothes


class Coat(AbstractClothes):

    def __init__(self, clothe_type="Coat", men_women_coat=None, coat_size=None):
        super().__init__(clothe_type)
        self.men_women_coat = men_women_coat
        self.coat_size = coat_size

    def cloth_spent(self, n):
        return round((n / 6.5 + 0.5), 2)

# __end_class_Coat__

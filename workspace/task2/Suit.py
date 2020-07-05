"""
    Класс Костюм
"""
from workspace.task2.AbstractClothes import AbstractClothes


class Suit(AbstractClothes):

    def __init__(self, clothe_type="Suit", men_women_suit=None, suit_size=None):
        super().__init__(clothe_type)
        self.men_women_suit = men_women_suit
        self.suit_size = suit_size

    def cloth_spent(self, n):
        return round((2 * n + 0.3), 2)

# __end_class_Suit__

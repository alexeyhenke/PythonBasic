"""
    Абстрактный класс Одежда
"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    _clothes_type = ""

    def __init__(self, clothe_type=None):
        self._clothes_type = clothe_type

    # расчет суммарного расхода ткани
    @abstractmethod
    def cloth_spent(self, n):
        pass

    # тип одежды: пальто, костюм, платье и т.д.
    @property
    def get_clothe_type(self):
        return self._clothes_type

# __end_class_AbstractClothes__
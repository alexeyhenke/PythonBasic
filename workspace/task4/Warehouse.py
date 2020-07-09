from abc import ABC, abstractmethod


class Warehouse(ABC):

    def __init__(self, whouse_class: str, whouse_name: str, railway=False, sea_pier=False):
        self.whouse_class = whouse_class
        self.whouse_name = whouse_name
        self.railway = railway
        self.sea_pier = sea_pier

    # @abstractmethod
    # def add_equipment(self, equipment):
    #     pass
    #
    # @abstractmethod
    # def giv_out_equipment(self, indx):
    #     pass

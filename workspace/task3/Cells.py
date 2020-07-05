"""
   number_of_cells - количество ячеек в клетке
"""


class Cells:

    def __init__(self, name: str, number_of_cells: int):
        self.name = name
        self.number_of_cells = number_of_cells
        print(f'Создана клетка {self.name} с количеством ячеек {self.number_of_cells}')

    # Сложение
    def __add__(self, other):
        if not isinstance(other, Cells):
            raise TypeError(f'[ERROR]: тип аргумента не соответствует ожидаемому.')
        return Cells(f'New Cell "{self.name} + {other.name}"', self.number_of_cells + other.number_of_cells)

    # Вычитание
    def __sub__(self, other):
        if not isinstance(other, Cells):
            raise TypeError(f'[ERROR]: тип аргумента не соответствует ожидаемому.')
        else:
            new_cell = (self.number_of_cells - other.number_of_cells)
            if new_cell > 0:
                return Cells(f'New Cell "{self.name} - {other.name}"', new_cell)
            else:
                print(f'[ERROR] Объект не создан. Вычитание "{self.name} - {other.name}" дает отрицательный результат.')

    # Умножение
    def __mul__(self, other):
        if not isinstance(other, Cells):
            raise TypeError(f'[ERROR]: тип аргумента не соответствует ожидаемому.')
        else:
            return Cells(f'New Cell "{self.name} * {other.name}"', self.number_of_cells * other.number_of_cells)

    # Деление
    def __truediv__(self, other):
        if not isinstance(other, Cells):
            raise TypeError(f'[ERROR]: тип аргумента не соответствует ожидаемому.')
        else:
            return Cells(f'New Cell "{self.name} // {other.name}"', self.number_of_cells // other.number_of_cells)

    # Группировка в ряды
    def make_order(self, cells_in_row):
        cell_in_last_row = self.number_of_cells % cells_in_row
        row_count = self.number_of_cells // cells_in_row
        order_str = ""

        for line in range(row_count):
            order_str += (f'*' * cells_in_row)
            order_str += "\n"

        order_str += (f'*' * cell_in_last_row)

        return order_str

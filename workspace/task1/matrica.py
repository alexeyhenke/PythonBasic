"""
    класс Matrix (матрица)
    принимает данные (список списков) для формирования матрицы
"""
from functools import reduce


class Matrica:

    def __init__(self, data_list: [[]]):
        self.matrix = data_list
        print(f'Создан объект Матрица: {self.matrix}')

    def __str__(self):
        result = ""
        for n in range(len(self.matrix)):
            for el in self.matrix[n][:]:
                result += f'{el} '

            result += "\n"

        return result

    def __add__(self, other):
        result = []
        if not isinstance(other, Matrica):
            raise TypeError(f'[ERROR]: тип аргумента не соответствует ожидаемому. {type(other).__name__}')

        if len(self.matrix[:]) == len(other.matrix[:]):
            for i in range(len(self.matrix[:])):
                row = []
                if len(self.matrix[i][:]) == len(other.matrix[i][:]):
                    for k in range(len(self.matrix[:][:])):
                        row.append(int(self.matrix[i][k]) + int(other.matrix[i][k]))
                    result.append(row)
                else:
                    raise IndexError(f'ERROR: Ошибка при сложении матриц. Количество элементов в ряду матриц не совпадает')
            return Matrica(result)
        else:
            raise IndexError(f'ERROR: Ошибка при сложении матриц. Количество строк матриц не совпадает')


# __end_class_Martix__
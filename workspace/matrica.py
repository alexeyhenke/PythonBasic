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

        min_len = len(self.matrix[:])

        for i in range(min_len):
            row = []
            for k in range(min_len):
                row.append(int(self.matrix[i][k]) + int(other.matrix[i][k]))
            result.append(row)

        return result

# __end_class_Martix__
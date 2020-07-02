"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
   который должен принимать данные (список списков) для формирования матрицы.

   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

   Примеры матриц вы найдете в методичке.

   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
   матриц). Результатом сложения должна быть новая матрица.

   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
   первым элементом первой строки второй матрицы и т.д.
"""
from matrica import Matrica

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы 'Matrix'!"))
print("= " * 50)

data_matrix_a = []
data_matrix_b = []
n_lines = 0

while True:
    n_lines = input("Введите размер матрицы A: ")

    if n_lines.isdigit():
        for i in range(int(n_lines)):
            print(f"Введите значения для {i + 1}-го ряда через пробел\n >", end=" ")
            data_matrix_a.append(list(map(int, input().split())))
        break
    else:
        print("Ошибка ввода. Введенное значение не цифра.")

while True:
    n_lines = input("Введите размер матрицы B: ")

    if n_lines.isdigit():
        for i in range(int(n_lines)):
            print(f"Введите значения для {i + 1}-го ряда через пробел\n >", end=" ")
            data_matrix_b.append(list(map(int, input().split())))
        break
    else:
        print("Ошибка ввода. Введенное значение не цифра.")

matrix_a = Matrica(data_matrix_a)
matrix_b = Matrica(data_matrix_b)

print(matrix_a)
print(matrix_b)
print("- " * 10)

data_matrix_c = (matrix_a + matrix_b)
matrix_c = Matrica(data_matrix_c)
print(matrix_c)

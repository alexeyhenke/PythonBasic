"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
   Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
   При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

   Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
   Второй — более сложная реализация без оператора **, предусматривающая использование цикла
"""
import math

num_a = 0
int_b = 0
result = 0
next_inter = True


def pow_variant1(a, n):
    return a ** n


def pow_variant2(a, n):
    if n == 0:
        return 1
    res = a
    if n < 0:
        for i in range((n + 1), 0, 1):
            res *= a
        return 1 / res
    else:
        for i in range((n - 1), 0, 1):
            res *= a
        return res


def isnegdigit(b):
    try:
        if b[:1] == '-':
            if b[1:].isdigit():
                return True
        else:
            return False
    except ValueError:
        return False


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while next_inter:

    while True:
        num_a = input("Введите положительное число А: ")
        if isfloat(num_a):
            num_a = float(num_a)
            break
        else:
            print(f'Ошибка ввода: {num_a} не число.')

    while True:
        int_b = input("Введите целое отрицательное число B: ")
        if isnegdigit(int_b):
            int_b = int(int_b)
            break
        else:
            print(f'Ошибка ввода: {int_b} повторите ещё раз.')

    print("- " * 50)
    print(f'Выполним возведение числа А "{num_a}" в степень значение B "{int_b}"')
    result = pow_variant1(num_a, int_b)
    print(f'Результат (вариант с помощью оператора **): {result}')
    result = pow_variant2(num_a, int_b)
    print(f'Результат (вариант с помощью цикла):\t\t{result}')
    check = math.pow(num_a, int_b)
    print(f'Проверка (использонание math.pow()): \t\t{check}')
    print("- " * 50)

    while True:
        next_add = input("Хотите выполнить дополнительный расчет (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")

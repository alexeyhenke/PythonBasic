"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
   и возвращает сумму наибольших двух аргументов.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу 'Расчитай число'"))
print("= " * 50)

int_a = 0
int_b = 0
int_c = 0
next_inter = True


def max_summ(int_a, int_b, int_c) -> int:
    """ Функция возвращает сумму наибольших двух аргументов
    :param int_a:
    :param int_b:
    :param int_c:
    :return int:
    """
    arg1 = 0
    arg2 = 0

    if int_a > int_c:
        arg1 = int_a
        if int_c > int_b:
            arg2 = int_c
        else:
            arg2 = int_b
    else:
        arg1 = int_c
        if int_a > int_b:
            arg2 = int_a
        else:
            arg2 = int_b

    return arg1 + arg2
# __end_max_summ

while next_inter:

    while True:
        int_a = input("Введите число А: ")
        if int_a.isdigit():
            int_a = int(int_a)
            break
        else:
            print(f'Ошибка ввода: {int_a} не число.')

    while True:
        int_b = input("Введите число B: ")
        if int_b.isdigit():
            int_b = int(int_b)
            break
        else:
            print(f'Ошибка ввода: {int_b} не число.')

    while True:
        int_c = input("Введите число C: ")
        if int_c.isdigit():
            int_c = int(int_c)
            break
        else:
            print(f'Ошибка ввода: {int_c} не число.')

    print("- " * 50)
    summ = max_summ(int_a, int_b, int_c)
    print(f'Сумма наибольших двух аргументов: {summ}')

    while True:
        next_add = input("Хотите выполнить дополнительный расчет (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")

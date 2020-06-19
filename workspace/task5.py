"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
   При нажатии Enter должна выводиться сумма чисел.
   Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
   Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение программы завершается.
   Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
   к полученной ранее сумме и после этого завершить программу.
"""

summ = 0
meta_symbol = ['!', '@', '#', '$', '%', '^', '&', '~']


def sum_number(input_str: str):
    split_str = input_str.split()
    result = 0
    for n in split_str:
        try:
            if n.isdigit():
                result += int(n)
            elif n in meta_symbol:
                print(f'В строке был найден спец.символ "{n}". Суммирование ряда завершается.')
                return result
            else:
                print(f'Ошибка ввода: значение "{n}" будет пропущено т.к. это не цифра')

        except TypeError as e:
            raise e

    return result


iscontinue = True

while iscontinue:
    input_str = input(f"Ведите строку чисел, разделенных пробелом "
                      f"\nдля завершения, введите один из символов {meta_symbol}: ")
    if input_str != '':
        summ += sum_number(input_str)
        print(f'Сумма чисел: {summ}')
        print('- ' * 50)
    else:
        print("Ошибка ввода: строка пустая")

    for n in input_str.split():
        if n in meta_symbol:
            iscontinue = False
            break

# -*- coding: UTF-8 -*-
"""
6. Реализовать два небольших скрипта:

   а) итератор, генерирующий целые числа, начиная с указанного,

   б) итератор, повторяющий элементы некоторого списка, определенного заранее.

   Подсказка: использовать функцию count() и cycle() модуля itertools.
   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
   Необходимо предусмотреть условие его завершения.

   Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
   Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
import itertools
import sys


def run(s=3, e=0) -> list:
    result_list = []
    if e == 0:
        e = s + 10

    for el in itertools.count(s):
        result_list.append(el)
        if el >= e:
            break

    return result_list


if __name__ == "__main__":
    param_counter = 1
    start_list = 0
    end_list = 0

    if len(sys.argv) == 1:
        print("По умолчанию: Скрипт выводит целые числа, начиная с 3, и при достижении числа 10 завершат работу\n"
              "Для получения справки '-h' или '--help'")
    elif len(sys.argv) == 2:
        param_name = sys.argv[1]
        if (param_name == "--help" or
                param_name == "-h"):
            print(f'Скрипт "itterator" генерирует целые числа, начиная с указанного\n'
                  f'В случае, если не задается граничное значение, "itterator" сформирует только 10 значений.\n'
                  f'Справка (keys):\n'
                  f'\t"-s" or "--start" \tначальное значение (начиная с указанного)\n'
                  f'\t"-e" or "--end" \tграничное значение для завершения\n'
                  f'\t"-h" or "--help"\tвывод на экран текущей справки')
        else:
            print("Ошибка. Неизвестный параметр '{}'".format(param_name))
            sys.exit(1)

    else:
        if len(sys.argv) < 3:
            print("Ошибка. Слишком мало параметров.")
            sys.exit(1)

        if len(sys.argv) > 5:
            print("Ошибка. Слишком много параметров.")
            sys.exit(1)

        param_name = ""
        param_value = ""

        while len(sys.argv) > param_counter:
            param_name = sys.argv[param_counter]
            param_value = sys.argv[param_counter + 1]

            if (param_name == "--start" or
                    param_name == "-s"):
                start_list = int(param_value)
            elif (param_name == "--end" or
                  param_name == "-e"):
                end_list = int(param_value)
            elif (param_name == "--help" or
                  param_name == "-h"):
                print(f'Скрипт "itterator" генерирует целые числа, начиная с указанного\n'
                      f'В случае, если не задается граничное значение, "itterator" сформирует только 10 значений.'
                      f'Справка (keys):\n'
                      f'\t"-s" or "--start" \tначальное значение (начиная с указанного)\n'
                      f'\t"-e" or "--end" \tграничное значение для завершения\n'
                      f'\t"-h" or "--help"\tвывод на экран текущей справки')
            else:
                print("Ошибка. Неизвестный параметр '{}'".format(param_name))
                sys.exit(1)

            param_counter += 2

    print(f'Список: {run(start_list, end_list)}')

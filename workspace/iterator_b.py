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


def run_cycle(cycle_list, repeation=0):
    input_string = cycle_list
    str_buffer = itertools.cycle(input_string)
    seq_repeation = 0
    seq_start = 0
    seq_end = len(cycle_list)

    for output in str_buffer:
        if seq_start == 0:
            print(f'Повтор: {seq_repeation + 1}')

        print(output, end=" ")

        if seq_start == (seq_end - 1):
            if seq_repeation >= repeation:
                break
            else:
                seq_repeation += 1
                seq_start = 0
                print("\n")
        else:
            seq_start += 1



if __name__ == "__main__":
    cycle_list = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    print(f'Исходный список элементов:')
    print(cycle_list)
    run_cycle(cycle_list)

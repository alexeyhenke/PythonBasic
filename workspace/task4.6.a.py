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

## а) итератор, генерирующий целые числа, начиная с указанного
## iterator_a.py
from workspace import iterator_a
from workspace import iterator_b

iter_list = iterator_a.run()
print(iter_list)
print("- " * 50)
## б) итератор, повторяющий элементы некоторого списка, определенного заранее
## iterator_b.py
cycle_list = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
iterator_b.run_cycle(cycle_list)

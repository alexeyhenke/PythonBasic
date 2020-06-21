"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

   Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

   Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

   Результат: [12, 44, 4, 10, 78, 123]
"""
import random

print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы выбора!"))
print("= " *50)
print("\nИсходный список:")
print("- " *50)
data_list = [(lambda i: i * i)(i) for i in random.choices(range(0, 8), k=10)]
print(f'{data_list}\n')

int_counter = 0
new_data_list = []
for i in data_list:
    if len(data_list) >= (int_counter + 1):
        if data_list[int_counter] < data_list[int_counter + 1]:
            new_data_list.append(data_list[int_counter + 1])
    else:
        break
    int_counter += 2

print("Результат выбора:")
print("- " *50)
if len(new_data_list) == 0:
    print("Выбранный список пуст, т.к. нет значений соответствующих условию (значения которых больше предыдущего элемента)")
else:
    print(new_data_list)

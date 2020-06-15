"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
   Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
   При нечетном количестве элементов последний сохранить на своем месте.
   Для заполнения списка элементов необходимо использовать функцию input().
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Скрипт перемешивания элементов списка!"))
print("= " * 50)

arr_indx = 0
array_list = []
element = ""
end = ''

print("Введите целочисленные значение")
while True:
    end = input("(для выхода нажмите 'Q/q'): ")
    if end == 'Q' or end == 'q':
        break

    if end.isdigit():
        array_list.append(end)
    else:
        print(f'Ошибка ввода: значение "{end}" не является числом. повторите еще раз.')

print(f'Вы ввели список значений: {list(array_list)}')

for element in array_list:
    if (arr_indx + 1) <= (len(array_list) - 1):
        array_list[arr_indx], array_list[arr_indx + 1] = array_list[arr_indx + 1], array_list[arr_indx]
        arr_indx += 2

print(f'Список после перемешивания: {list(array_list)}')
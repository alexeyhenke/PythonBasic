"""
1. Создать список и заполнить его элементами различных типов данных.
   Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
   Элементы списка можно не запрашивать у пользователя, а указать явно, в программе
"""

print("= " * 50)
print("{greeting:^100}".format(greeting="Скрипт проверки типа данных каждого элемента списка!"))
print("= " * 50)
# -= variables block =-
# String
a_str = "Hello world!"
# Integer
b_int = 123
# Floating
c_float = 3.14
# Boolean
d_bool = True
# NoneType
x_none = None

my_list = [a_str, b_int, c_float, d_bool, x_none]
print("Элементы списка: \n")
print(my_list)

for element in my_list:
    if type(element) == bool:
        print("= " * 50)
        print(f'Determine type of element {element}: {type(element)}')
        print(f'Type of element "{element}" is Boolean')
    elif type(element) == int:
        print("= " * 50)
        print(f'Determine type of element {element}: {type(element)}')
        print(f'Type of element "{element}" is Integer')
    elif type(element) == str:
        print("= " * 50)
        print(f'Determine type of element {element}: {type(element)}')
        print(f'Type of element "{element}" is String')
    elif type(element) == float:
        print("= " * 50)
        print(f'Determine type of element {element}: {type(element)}')
        print(f'Type of element "{element}" is Floating')
    elif x_none is None:
        print("= " * 50)
        print(f'Determine type of element {element} by type() method: {type(element)}')
        print(f'Type of element "{element}" is NoneType')
    else:
        print("= " * 50)
        print(f'Determine type of element {element} by type() method: {type(element)}')

print("= " * 50)

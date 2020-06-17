"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу приложения выполняющую деление чисел!"))
print("= " * 50)

number_a = 0
number_b = 0


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"[ERROR]: {e}")


while True:
    input_number = input("Ведите значение А: ")
    if input_number.isdigit():
        number_a = float(input_number)
        break
    else:
        print(f'Ошибка ввода: введенное значение {input_number} не является числом')

while True:
    input_number = input("Ведите значение B: ")
    if input_number.isdigit():
        number_b = float(input_number)
        break
    else:
        print(f'Ошибка ввода: введенное значение {input_number} не является числом')

result = division(number_a, number_b)

print("- " * 50)
print(f'Результат деления числа  {number_a} на {number_b} является {result}')

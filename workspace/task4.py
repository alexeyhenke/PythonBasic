"""
4. Пользователь вводит целое положительное число.
   Найдите самую большую цифру в числе.
   Для решения используйте цикл while и арифметические операции.
"""
print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу 'Поиск наибольшей цифры в числе'"))
print("= " *50)

int_number = 0
max_digit = 0
int_number_length = 0

while True:
    int_number = input("Введите целое положительное число: ")

    if int_number.isdigit():
        int_number = int(int_number)
        if int_number < 0:
            print("Ошибка ввода. Введите целое положительное число еще раз.")
        else:
            break
    else:
        print("Ошибка ввода. Введите целое положительное число еще раз.")

report = f'Вариант №1: Максимальное цифра в числе "{int_number}" является "{max(str(int_number))}"'
print(report)

while len(str(int_number)) > int_number_length:
    int_digit = int(str(int_number)[int_number_length])
    if max_digit < int_digit:
        max_digit = int_digit

    int_number_length += 1

report = f'Вариант №2: Максимальное цифра в числе "{int_number}" является "{max_digit}"'
print(report)
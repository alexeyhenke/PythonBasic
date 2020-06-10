"""
3. Узнайте у пользователя число n.
   Найдите сумму чисел n + nn + nnn.
   Например, пользователь ввёл число 3.
   Считаем 3 + 33 + 333 = 369
"""
print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу 'Расчитай число'"))
print("= " *50)

user_number = 0
str_number = ""
int_number = 0

while True:
    user_number = input("Введите любое число от 1 до 10: ")

    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0:
            print("Ошибка ввода. Введенное число меньше 0 или равное 0.\nВведите любое число от 1 до 10 еще раз")
        elif user_number > 10:
            print("Ошибка ввода. Введенное число больше 10.\nВведите любое число от 1 до 10 еще раз")
        else:
            break
    else:
        print("Ошибка ввода. Введите любое число от 0 до 10 еще раз")

for i in range(user_number):
    str_number += str(user_number)
    int_number += int(str_number)   # Считаем 3 + 33 + 333 = 369

print(int_number)
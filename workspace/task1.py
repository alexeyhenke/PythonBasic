"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
   запросите у пользователя несколько чисел и строк и сохраните в переменные,
   выведите на экран.
"""
user_fname = ""
user_sname = ""
user_age = 0

print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу опросника!"))
print("= " *50)

while True:
    user_fname = input("Представьтесь пожалуйста.\nНазовите свое имя: ")
    if user_fname != "":
        break
    else:
        print("Извините, Вы ничего не ввели в поле Имя. Попробуйте еще раз\n")

while True:
    user_sname = input("Введите Вашу фамилию: ")
    if user_sname != "":
        break
    else:
        print("Извините, Вы ничего не ввели в поле Фамилия. Попробуйте еще раз\n")

while True:
    user_age = input("Введите Ваш возраст: ")
    if user_age.isdigit():
        user_age = int(user_age)
        break
    else:
        print("Ошибка ввода. Введите Ваш возраст еще раз\n")

answer_str = f'Добрый день {user_fname} {user_sname} Вам {user_age} лет Вы родились в {2020 - user_age} году.'
print("= " *50)
print(answer_str)
print("= " *50)

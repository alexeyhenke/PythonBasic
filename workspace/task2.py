"""
2. Пользователь вводит время в секундах.
   Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
   Используйте форматирование строк
"""
print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу перевода время в часы, минуты и секунды!"))
print("= " *50)

input_seconds = 0

while True:
    input_seconds = input("Введите время в секундах: ")

    if input_seconds.isdigit():
        input_seconds = int(input_seconds)
        break
    else:
        print("Ошибка ввода. Введите время в секундах еще раз.")

calc_hours = input_seconds // 3600
calc_minutes = (input_seconds % 3600) // 60
calc_seconds = (input_seconds % 3600) % 60

calc_result = f"Получили время (в формате чч:мм:сс): {str(calc_hours).rjust(2,'0')}:{str(calc_minutes).rjust(2,'0')}:{str(calc_seconds).rjust(2,'0')}"
print(calc_result)

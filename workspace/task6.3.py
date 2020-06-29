"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
   Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
   оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.

   В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
   Проверить работу примера на реальных данных (создать экземпляры класса Position,
   передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""
print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы Worker (работник)"))
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
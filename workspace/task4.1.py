"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
   В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.

   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу расчета заработной платы!"))
print("= " * 50)

# query_template = {'часы': ('количество отработанных часов', float)
#     , 'ставка': ('ставку в час', float)
#     , 'премия': ('премию', float)}


# def calc_payment(data: dict) -> float:
#     """
#     Функция расчета заработной платы сотрудника
#     :param float_hours:
#     :param float_price:
#     :param float_bonus:
#     :return float:
#     """
#     float_hours = 1.0
#     float_price = 5.25
#     float_bonus = 0.0
#
#     for key, value in data.items():
#         if key == 'часы':
#             float_hours = value
#         elif key == 'ставка':
#             float_price = value
#         elif key == 'премия':
#             float_bonus = value
#         else:
#             print(f'ERROR: не ожидаемый параметр {value}')
#
#     return round((float_hours * float_price) + float_bonus, 2)


# def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False
#

def payment(hours, price, bonus):
    return round((hours * price) + bonus, 2)


_, user_hour, user_price, user_bonus, *__ = argv

user_salary = str(payment(float(user_hour), float(user_price), float(user_bonus))).rjust(2, '0')
print(f"Зарплата текущего сотрудника ${user_salary}")
print("- " * 50)

# Первая реализация, не понял в задании, что нужна реализация с запуском из консоли
#   (попробовал применить шаблон - мне понравилось, хотя и заморочно)
# user_hours = 0.0
# user_price = 0.0
# user_bonus = 0.0
# user_payme = {}
# go_next = True
#
# while go_next:
#     for key, value in query_template.items():
#         while True:
#             user_input = input(f'Введите {value[0]} сотрудника: ')
#             if isfloat(user_input):
#                 try:
#                     user_input = value[1](user_input)
#                 except ValueError as e:
#                     print("Ошибка ввода: вы ввели не верное значение")
#                     continue
#                 user_payme[key] = user_input
#                 break
#             else:
#                 print("Ошибка ввода: Попробуйте еще раз\n")
#
#     print("- " * 50)
#     user_salary = str(calc_payment(user_payme)).rjust(2,'0')
#     print(f"Зарплата текущего сотрудника ${user_salary}")
#
#     while True:
#         calc_next = input("Расчитать следующего сотрудника (да / нет): ")
#         if calc_next.lower() in ('да', 'нет'):
#             go_next = calc_next.lower() == 'да'
#             break
#         else:
#             print("Ошибка ввода: ответьте 'да' или 'нет'.")

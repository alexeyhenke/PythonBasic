"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
   Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
   Класс-исключение должен контролировать типы данных элементов списка
"""


class ExceptionType(Exception):

    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def isdigit_check(value):
        return value.isdigit()


# __end_class_ExceptionType__

if __name__ == '__main__':
    number_list = []

    while True:
        x = (input("Введите число или 'q' для выхода: "))
        try:
            if x == 'q':
                print("Программа завершена")
                print("- " * 30)
                break
            else:
                if not ExceptionType.isdigit_check(x):
                    raise ExceptionType(f'[ERROR] Значение "{x}" не является цифрой')
                else:
                    number_list.append(x)
                    print(f'Список: {number_list}')
                    print("- " * 30)

        except ExceptionType as ex:
            print(ex)
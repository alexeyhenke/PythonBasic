"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
   В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
   и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
   месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
from datetime import datetime


class Data:
    date_format = "%d-%m-%Y"

    data_list = []

    def __init__(self, data_str: str):
        self.data_str = data_str

    @classmethod
    def split_to_int(cls, data_str):
        cls.data_list.clear()
        for num in data_str.split('-'):
            if num.isdigit():
                cls.data_list.append(int(num))

        return cls.data_list

    @staticmethod
    def validate_data(data_str, date_format):
        try:
            if datetime.strptime(data_str, date_format):
                print(f'Указанная дата {data_str} указана верно.')
        except ValueError as e:
            print(f'Указана не корректная дата {data_str}. Дата задается в формате ДД-ММ-ГГГГ.\n{e}')


if __name__ == '__main__':
    print("= " * 50)
    my_data = Data("02-04-2012")
    my_data.split_to_int(my_data.data_str)
    Data.validate_data(my_data.data_str, my_data.date_format)
    print("= " * 50)
    my_data = Data("02-14-2012")
    my_data.split_to_int(my_data.data_str)
    Data.validate_data(my_data.data_str, my_data.date_format)
    print("= " * 50)

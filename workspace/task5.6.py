"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
   практических и лабораторных занятий по этому предмету и их количество.
   Важно, чтобы для каждого предмета не обязательно были все типы занятий.
   Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
   Вывести словарь на экран.

    Примеры строк файла:

    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —
    Пример словаря:

    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from os import path

print(" =" * 50)
print("{greeting:^100}".format(
    greeting="Программа формирует словарь, содержащий название предмета и общее количество занятий по нему"))
print(" =" * 50)

file_name = 'file_task5.6.txt'
file_path = path.join(path.dirname(__file__), 'files', file_name)

schedule_dict = {}
key = ""
value_dict = 0

with open(file_path, 'rt', encoding='UTF-8') as file_rt:
    for el in file_rt.read().split(' '):
        if el[-1] == ':':
            key = el.strip(' \t\n\r-:')
            value_dict = 0
        else:
            num = el.split('(')
            for x in num:
                if x.isdigit():
                    value_dict += int(x.strip())

        schedule_dict[key] = value_dict

print(f'Расписание:')
for key, value in schedule_dict.items():
    print(f'{key} - {value} занятий')

print("- " * 50)

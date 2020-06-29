"""
4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4

   Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
   При этом английские числительные должны заменяться на русские.
   Новый блок строк должен записываться в новый текстовый файл
"""
from os import path

print(" =" * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в программу переводчик!"))
print(" =" * 50)

dict_en_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

en_file_name = 'file_task5.4_eng.txt'
ru_file_name = 'file_task5.4_rus.txt'
en_file_path = path.join(path.dirname(__file__), 'files', en_file_name)
ru_file_path = path.join(path.dirname(__file__), 'files', ru_file_name)

# проверим, существует ли файл
try:
    with open(en_file_path) as file:
        print(f'SUCCESS: file is exists: \n\t{en_file_path}')
except IOError as e:
    print(f'ERROR: No such file or directory: {e}')

num_eng_txt = ""
num_number = ""
str_ru = ""


def insert_into_ru_file(string):
    with open(ru_file_path, 'w', encoding='UTF-8') as ru_file:
        ru_file.write(string)


def print_file(title_msg, ru_file_path):
    with open(ru_file_path, 'r', encoding='UTF-8') as file:
        print("- " * 50)
        print(f'{title_msg}:')

        for line in file:
            print(line, end="")


with open(en_file_path, 'r') as eng_file:
    print("- " * 50)
    print(f'Содержимое EN файла:')

    for line in eng_file:
        print(line, end="")
        el_list = line.split()
        num_eng_txt = el_list[0]
        num_number = el_list[-1]

        for key, value in dict_en_ru.items():
            if num_eng_txt.capitalize() == key.capitalize():
                str_ru += f'{value} - {num_number}\n'

insert_into_ru_file(str_ru)
print_file('Содержимое RU файла', ru_file_path)

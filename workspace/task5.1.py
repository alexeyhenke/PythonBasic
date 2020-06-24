"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
   вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
from os import path

print(" =" * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу создания и заполнения файла!"))
print(" =" * 50)

file_name = 'file_task5.1.txt'
file_path = path.join(path.dirname(__file__), 'files', file_name)

# создадим файл без лишних проверок
file = open(file_path, 'w', encoding='UTF-8')
print(f'Создан файл: \n{file_path}')
file.close()

while True:
    try:
        user_str = input("Введите текст для записи в файл (для выхода введите пробел без текста):")
        if (user_str[0] != " ") and len(user_str) >= 1:
            file = open(file_path, 'at', encoding='UTF-8')
            file.write(user_str + '\n')
        else:
            break
    except Exception as e:
        print(f'Не предвиденная ошибка: {e}')
    finally:
        file.close()



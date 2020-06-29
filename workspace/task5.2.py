"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
   выполнить подсчет количества строк, количества слов в каждой строке
"""
from os import path

print(" =" * 50)
print("{greeting:^100}".format(greeting="Выполнить подсчет количества строк, количества слов в каждой строке!"))
print(" =" * 50)

file_name = 'file_task5.2.txt'
file_path = path.join(path.dirname(__file__), 'files', file_name)

try:
    with open(file_path) as file:
        print(f'SUCCESS: file is exists: \n\t{file_path}')
except IOError as e:
    print(f'ERROR: No such file or directory: {e}')

# выполнить подсчет количества строк, количества слов в каждой строке
line_counter = 0
word_counter = 0

try:
    with open(file_path, 'r') as file:
        print("- " * 50)
        for line in file:
            line_counter += 1
            print(line, end="")
            # print(f'Строка №{line_counter} имеет {len(line.split(" "))} слов')
            word_counter += len(line.split(" "))

        print("- " * 50)
        print(f'Количество строк: {line_counter}')
        print(f'Файл содержит {word_counter} слов')
except IOError as e:
    print(f'ERROR: {e}')
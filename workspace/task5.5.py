"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
   Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
from os import path

print(" =" * 50)
print("{greeting:^100}".format(
    greeting="Добро пожаловать! Программа подсчитывает сумму чисел в файле и выводить ее на экран"))
print(" =" * 50)

file_name = 'file_task5.5.txt'
file_path = path.join(path.dirname(__file__), 'files', file_name)
new_sum = 0
file_content = ""

# Создать (программно) текстовый файл
with open(file_path, 'wt', encoding='UTF-8') as file_wt:
    file_wt.close()

# записать в него программно набор чисел
with open(file_path, 'at', encoding='UTF-8') as file_at:
    for el in [(lambda i: i * i)(i) for i in random.choices(range(0, 8), k=10)]:
        file_at.write(f'{el} ')
        file_content += f'{el} '

    file_at.close()

try:
    file = open(file_path, 'rt', encoding='UTF-8')
    print("- " * 50)
    new_sum = sum(map(int, file.read().split()))
    file.close()
except IOError as e:
    print(f'ERROR: {e}')


print(f'Содержимое файла: {file_content}')
print("- " * 50)
print(f'Сумма всех значений находящихся в файле: {new_sum}')

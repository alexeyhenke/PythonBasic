"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
   Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
   Выполнить подсчет средней величины дохода сотрудников
"""
from os import path

print(" =" * 50)
print("{greeting:^100}".format(greeting="Выполнить подсчет средней величины дохода сотрудников!"))
print(" =" * 50)

file_name = 'file_task5.3.txt'
file_path = path.join(path.dirname(__file__), 'files', file_name)

# проверим, существует ли файл
try:
    with open(file_path) as file:
        print(f'SUCCESS: file is exists: \n\t{file_path}')
except IOError as e:
    print(f'ERROR: No such file or directory: {e}')

users_name = []
user_name = []
user_counter = 0
user_salary = 0
avg_salary = 0.0

# вывести полный список сотрудников
with open(file_path, 'r') as r_file:
    print("- " * 50)

    for line in r_file:
        print(line, end="")
        user_name, user_salary = (line.split(" "))

        user_salary = int(user_salary)
        if user_salary < 20000:
            users_name.append(user_name)

        avg_salary += user_salary
        user_counter += 1

print("- " * 50)
print(f'Сотрудники у которых З/П меньше 20 т.р.: {users_name}')
print(f'Средняя З/П сотрудников: {avg_salary / user_counter}')
print("- " * 50)


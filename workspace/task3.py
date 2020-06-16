"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
   Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
   Напишите решения через list и через dict.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Скрипт сообщает к какому времени года относится месяц"))
print("= " * 50)

winter_arr = ['Зима', 1, 2, 12]
spring_arr = ['Весна', 3, 4, 5]
summer_arr = ['Лето', 6, 7, 8]
autumn_arr = ['Осень', 9, 10, 11]
seasons_arr = [winter_arr, spring_arr, summer_arr, autumn_arr]
seasons_dict = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

while True:
    number_of_month = input("Введите номер месяца в виде целого числа (от 1 до 12): ")
    if number_of_month.isdigit():
        number_of_month = int(number_of_month)
        if (number_of_month >= 1) and (number_of_month <= 12):
            break
        else:
            print(f'Указанное значение {number_of_month} не входит в диапазон от 1 до 12')
    else:
        print(f'Ошибка ввода: "{number_of_month}" не является числом')

# вывести время года: решение через list
#print(seasons_arr)
for season in seasons_arr:
    if number_of_month in season:
        print("= " * 50)
        print(f'Указанный месяц соответствует сезону (решение через list): "{season[0]}"\n\n')

# вывести время года: решение через dict
#print(seasons_dict.items())
for key in seasons_dict.keys():
    if number_of_month in seasons_dict.get(key):
        print(f'Указанный месяц соответствует сезону (решение через dict): "{key}"')
        print("= " * 50)

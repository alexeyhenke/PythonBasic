"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

   Подсказка: использовать функцию range() и генератор.
"""
print("= " *50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу 'найти числа, кратные 20 или 21' в пределах от 20 до 240"))
print("= " *50)

data_list = [i for i in range(20, 240) if ((i % 20) == 0) or ((i % 21) == 0)]
print(data_list)
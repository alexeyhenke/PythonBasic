"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
   У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
   то новый элемент с тем же значением должен разместиться после них.

    Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
    Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.

    Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.

    Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

    Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="«Рейтинг»"))
print("= " * 50)

rating_list = [7, 5, 3, 3, 2]
last_pos = 0
customs_rating = 0
index_list = 0

print(f'Начальный список рейтинга: {rating_list}\n')

while True:
    customs_rating = input("Введите свой оценочный рейтинг (целочисленное значение) или для выхода нажмите 'Q/q': ")
    if customs_rating == 'Q' or customs_rating == 'q':
        break

    if customs_rating.isdigit():
        customs_rating = int(customs_rating)
        if customs_rating in rating_list:
            print(f'Ваш Рейтинг "{customs_rating}" будет помещен в список')
            last_pos = rating_list.index(customs_rating) + (rating_list.count(customs_rating) - 1)
            rating_list.insert((last_pos + 1), customs_rating)
        else:
            while len(rating_list) > index_list:
                if rating_list[index_list] > customs_rating:
                    if len(rating_list) == (index_list + 1):
                        rating_list.append(customs_rating)
                        break
                    else:
                        index_list += 1
                else:
                    rating_list.insert(index_list, customs_rating)
                    break
    else:
        print(f'Ошибка ввода: введенное значение не является цифрой')

    index_list = 0
    print(f'Обновленный список рейтинга: {rating_list}')
    print("= " * 50)

# __EOF__

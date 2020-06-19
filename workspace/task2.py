"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
   имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в программу сохраняющая данные пользователя!"))
print("= " * 50)

users_list = []
next_inter = True
user_fname = ['Имя']
user_lname = ['Фамилия']
user_yearofborn = ['Год рождения']
user_city = ['Город проживания']
user_email = ['E-Mail']
user_phone = ['Телефон']

def createUsersList(user_fname: list, user_lname: list, user_yearofborn: list, user_city: list, user_email: list,
                    user_phone: list) -> list:
    user_row = {user_fname[0]: user_fname[1]
        , user_lname[0]: user_lname[1]
        , user_yearofborn[0]: user_yearofborn[1]
        , user_city[0]: user_city[1]
        , user_email[0]: user_email[1]
        , user_phone[0]: user_phone[1]}

    users_list.append(user_row)
    return users_list


while next_inter:
    user_row = {}

    while True:
        user_value = input("Ведите 'Имя' пользователя: ")
        if user_value != "":
            user_fname.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Имя' пустое.")

    while True:
        user_value = input("Ведите 'Фамилию' пользователя: ")
        if user_value != "":
            user_lname.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Фамилия' пустое.")

    while True:
        user_value = input("Ведите 'Год рождения' пользователя (YYYY): ")
        if user_value != "":
            user_yearofborn.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Год рождения' пустое.")

    while True:
        user_value = input("Ведите 'Город проживания' пользователя: ")
        if user_value != "":
            user_city.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Город проживания' пустое.")

    while True:
        user_value = input("Ведите 'E-Mail' пользователя: ")
        if user_value != "":
            user_email.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'E-Mail' пустое.")

    while True:
        user_value = input("Ведите 'Телефон' пользователя: ")
        if user_value != "":
            user_phone.append(user_value)
            break
        else:
            print("Ошибка ввода: поле 'Телефон' пустое.")

    users_list = createUsersList(user_fname, user_lname, user_yearofborn, user_city, user_email, user_phone)

    while True:
        next_add = input("Хотите добавить дополнительного пользователя? (Да / Нет): ")
        if next_add.lower() in ('да', 'нет'):
            next_inter = next_add.lower() == 'да'
            break
        else:
            print("Ошибка ввода: введите ответ еще раз")

print("- " * 50)
print(users_list)

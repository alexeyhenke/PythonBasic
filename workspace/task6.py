"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
   Каждый кортеж хранит информацию об отдельном товаре.
   В кортеже должно быть два элемента — номер товара и словарь с параметрами
   (характеристиками товара: название, цена, количество, единица измерения).

   Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в структуру данных «Товары»!"))
print("= " * 50)

products = tuple()
product_name = ""
product_price = 0.0
product_count = 0
product_unit = ""


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print("\n{title:^100}".format(title="Добавление товара"))
while True:
    product_name = input("Введите наименование товара: ")
    price = input("Введите цену товара: ")

    while not isfloat(price):
        print(f'Введенное значение "{price}" не является цифрой')

    product_price = float(price)

    count = input("Введите количество товара: ")
    while not count.isdigit():
        print(f'Введенное значение "{count}" не является цифрой')

    product_count = int(count)

    product_unit = input("Введите единицу измерения товара (кг/шт): ")

# не успел.
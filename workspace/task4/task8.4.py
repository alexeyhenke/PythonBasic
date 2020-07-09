from workspace.task4.OfficeEquipment import OfficeEquipment


print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу «Склад оргтехники»!"))
print("= " * 50)

equip_template = {
    'Brand': ("Брэнд", str),
    'Model': ("Модель", str),
    'Quantity': ("Количество", int),
    'Unit': ("Единицу измерения", str)
}
go_next = True
equipment_list = []
equipment_count = 1
product = {}

wh_printers = OfficeEquipment("A", "Склад притеров", True, False, "printer")
wh_printers.get_warehouse_info()


while go_next:
    product.clear()
    for key, value in equip_template.items():
        while True:
            user_input = input(f'Введите {value[0]} товара: ')
            try:
                user_input = value[1](user_input)
            except ValueError as e:
                print("Ошибка ввода: вы ввели не верное значение")
                continue
            product[key] = user_input
            break

    wh_printers.products.append(product)
    equipment_count += 1

    print("- " * 50)

    while True:
        calc_next = input("Вы хотите добавить товар? (да / нет): ")
        if calc_next.lower() in ('да', 'нет'):
            go_next = calc_next.lower() == 'да'
            break
        else:
            print("Ошибка ввода: ответьте 'да' или 'нет'.")

print("- " * 50)
print(f'Остатки по складу "{wh_printers.whouse_name}":')

print(wh_printers.get_products_list)
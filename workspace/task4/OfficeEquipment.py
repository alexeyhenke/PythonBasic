from workspace.task4.Warehouse import Warehouse


class OfficeEquipment(Warehouse):

    products = [[]]

    def __init__(self, whouse_class, whouse_name, railway, sea_pier, equip_type):
        super().__init__(whouse_class, whouse_name, railway, sea_pier)
        self.equip_type = equip_type

    def get_warehouse_info(self):
        print("{decor}{info:>20}".format(decor="- " * 40, info="Карточка склада"))
        print("{label:>30}{info:>70}".format(label=f'Наименование склада:', info=f'{self.whouse_name}'))
        print("{label:>30}{info:>70}".format(label=f'Класс склада:', info=f'{self.whouse_class}'))
        print("{label:>30}{info:>70}".format(label=f'Склад для хранения:', info=f'{self.equip_type}'))
        print("{label:>30}{info:>70}".format(label=f'Наличие Ж/Д путей:', info=f'{("Да", "Нет")[self.railway]}'))
        print(
            "{label:>30}{info:>70}".format(label=f'Наличие морского причала:', info=f'{("Да", "Нет")[self.sea_pier]}'))
        print(f'- ' * 50)



    def get_products_list(self):
        return self.products
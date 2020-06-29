"""
 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
    и завершать скрипт.
"""
import time

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы TrafficLight (светофор)!"))
print("= " * 50)


class TrafficLight:
    __color = ""

    def __init__(self):
        __color = "Red"
        print(f'Светофор включен. Горит {__color} свет')

    def _print_red(self):
        print("- " * 10)
        print("\033[31m {}".format('Red'))
        time.sleep(7)

    def _print_yellow(self):
        print("- " * 10)
        print("\033[33m {}".format('Yellow'))
        time.sleep(2)

    def _print_green(self):
        print("- " * 10)
        print("\033[32m {}".format('Green'))
        time.sleep(5)

    def running(self):
        count_down = 3
        while count_down > 0:
            self._print_red()
            self._print_yellow()
            self._print_green()
            count_down -= 1


trafficlight = TrafficLight()
time.sleep(1)
trafficlight.running()
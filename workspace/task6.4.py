"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
   Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
   Для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
   Выполните вызов методов и также покажите результат
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу программы 'Тачки' "))
print("= " * 50)


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина "{self.name}" начала своё движение со скоростью {self.speed} км/час')

    def stop(self):
        print(f'Машина "{self.name}" закончила своё движение')

    def turn(self, direction):
        if direction == "left":
            print(f'Машина "{self.name}" поворачивает влево.')
        else:
            print(f'Машина "{self.name}" поворачивает вправо.')

    def speed_up(self, increase):
        self.speed += increase
        print("Ускоряемся...", end=" ")
        self.show_speed()

    def speed_down(self, increase):
        self.speed -= increase
        print("Замедляемся...", end=" ")
        self.show_speed()

    def show_speed(self):
        print(f'Скорость "{self.name}" составляет {self.speed} км/час')


# __end_class_Car__


class TownCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        super().__init__(speed, color, name)
        self.speed_limit = speed_limit

    def show_speed(self):
        print(f'Скорость "{self.name}" составляет {self.speed} км/час')
        if self.speed > self.speed_limit:
            print(f'Внимание: "{self.name}" едет с превышением скорости на {self.speed - self.speed_limit} км/час')


# __end_class_TownCar__


class SportCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        super().__init__(speed, color, name)
        self.speed_limit = speed_limit

    def show_speed(self):
        print(f'Скорость "{self.name}" составляет {self.speed} км/час')
        if self.speed > self.speed_limit:
            print(f'Внимание: "{self.name}" едет с превышением скорости на {self.speed - self.speed_limit} км/час')

# __end_class_SportCar__


class WorkCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        super().__init__(speed, color, name)
        self.speed_limit = speed_limit

    def show_speed(self):
        print(f'Скорость "{self.name}" составляет {self.speed} км/час')
        if self.speed > self.speed_limit:
            print(f'Внимание: "{self.name}" едет с превышением скорости на {self.speed - self.speed_limit} км/час')


# __end_class_WorkCar__


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# __end_class_PoliceCar__

taxi = TownCar(10, 'Yellow', 'Taxi', 60)
taxi.go()
taxi.show_speed()
major = SportCar(60, 'Red', 'Ferrari SF90', 90)
major.go()
major.show_speed()
print("- " * 10)
taxi.speed_up(60)
print("- " * 10)
major.speed_up(100)
print("- " * 10)
town_car = TownCar(5, 'Blue', 'Volvo', 60)
town_car.go()
town_car.speed_up(20)


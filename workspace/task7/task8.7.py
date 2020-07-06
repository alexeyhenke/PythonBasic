"""
7. Реализовать проект «Операции с комплексными числами».
   Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
   Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу «Операции с комплексными числами»!"))
print("= " * 50)


class ComplexNumber:

    def __init__(self, a, b, *args):
        self.a = a  # действительная часть
        self.b = b  # мнимая часть
        self.z = 'a + bi'  # i мнимая единица

    def __add__(self, other):
        return f'Результат суммы комплексных чисел: Z ' \
               f'= {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Результат умножения комплексных чисел: Z ' \
               f'= {(self.a * other.a) - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'Z = {self.a} + {self.b}i'


# __end_class_ComplexNumber__

if __name__ == '__main__':
    complex_A = ComplexNumber(2, 5)
    complex_B = ComplexNumber(1, 2)

    print(f'«Комплексное число» A: {complex_A}')
    print(f'«Комплексное число» B: {complex_B}')
    print(complex_A + complex_B)
    print(complex_A * complex_B)

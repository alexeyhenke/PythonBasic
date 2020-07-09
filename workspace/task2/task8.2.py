"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
   Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
   должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZerro(Exception):
    def __init__(self, text):
        self.text = text


# __end_class_DivisionByZerro__

if __name__ == '__main__':
    result = 0.0
    while True:
        try:
            numberA = input("Введите число А или 'q' для выхода: ")
            if numberA.isdigit():
                numberB = input("Введите число B: ")
                if numberB.isdigit():
                    print("- " * 30)
                    try:
                        if not int(numberB):
                            raise DivisionByZerro("ERROR: ... division by zero")
                        else:
                            result = int(numberA) / int(numberB)
                            print(f'Результат деления: {numberA} / {numberB} = {result}')
                            print(". " * 30)
                    except DivisionByZerro as e:
                        print(e)
                else:
                    print(f'Введеное значение не цифра {numberB} Повторите попытку')
            else:
                if 'q'.capitalize() == numberA.capitalize():
                    break
                else:
                    print(f"Введеное значение не цифра {numberA} Повторите попытку")
        except Exception as ex:
            print("Error! {0}".format(ex))

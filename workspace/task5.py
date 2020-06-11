"""
5. Запросите у пользователя значения выручки и издержек фирмы.
   Определите, с каким финансовым результатом работает фирма
   (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
   Выведите соответствующее сообщение.

   Если фирма отработала с прибылью, вычислите рентабельность выручки
   (соотношение прибыли к выручке).
   Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в приложение расчета эффективности работы компании!"))
print("= " * 50)

float_proceed = 0.0  # значение выручки
float_expenses = 0.0  # значение издержек
float_fin_result = 0.0  # окончательный финансовый результат
int_number_of_employees = 0  # численность сотрудников фирмы
profitability = 0 # рентабельность
input_value = 0
str_report = ""


# число может быть дробное (дернул с stackoverflow)
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


while True:
    input_value = input("Введите сумму выручки Вашей фирмы: ")

    if isfloat(input_value):
        float_proceed = float(input_value)
        break
    else:
        print("Ошибка ввода. Введите сумму выручки еще раз.")

while True:
    input_value = input("Введите сумму издержек Вашей фирмы: ")

    if isfloat(input_value):
        float_expenses = float(input_value)
        break
    else:
        print("Ошибка ввода. Введите сумму издержек еще раз.")

while True:
    input_value = input("Введите количество сотрудников Вашей фирмы: ")

    if input_value.isdigit():
        int_number_of_employees = int(input_value)
        break
    else:
        print("Ошибка ввода. Введите количество сотрудников еще раз.")

if float_proceed > float_expenses:
    profitability = ((float_proceed - float_expenses) / float_proceed) * 100
    float_fin_result = float_proceed - float_expenses
    str_report = f'Поздравляю, прибыль Вашей фирмы составляет:\t${float_fin_result:.2f}\n' \
                 f'На каждого сотрудника приходится по \t\t${(float_fin_result / int_number_of_employees):.2f}\n' \
                 f'Рентабельность Вашего бизнеса составляет: \t{profitability:.1f}%'
elif float_proceed == float_expenses:
    str_report = f'Ваша фирма работает в 0 (ноль) Вам стоит задуматься'
else:
    profitability = ((float_proceed - float_expenses) / float_proceed) * 100
    float_fin_result = float_proceed - float_expenses
    str_report = f'Ваша фирма работает в убыток на сумму: \t\t${float_fin_result:.2f}\n' \
                 f'На каждого сотрудника приходится по \t\t${(float_fin_result / int_number_of_employees):.2f}\n' \
                 f'Рентабельность Вашего бизнеса составляет: \t{profitability:.1f}%'

print("= " * 50)
print(str_report)
print("= " * 50)
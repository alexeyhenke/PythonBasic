"""
6. Спортсмен занимается ежедневными пробежками.
   В первый день его результат составил a километров.
   Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
   Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
   Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня

   Например: a = 2, b = 3.

   Результат:
  1-й день: 2
  2-й день: 2,2
  3-й день: 2,42
  4-й день: 2,66
  5-й день: 2,93
  6-й день: 3,22
  Ответ: на 6-й день спортсмен достиг результата — не менее 3 км
"""
print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать в приложение составления плана тренировки!"))
print("= " * 50)


# число может быть дробное (дернул с stackoverflow)
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


start_distance = 0.0
target_distance = 0.0
days_counter = 1

while True:
    input_value = input("Укажите дистанцию пробежки с которой Вы начнете (км): ")
    if isfloat(input_value):
        start_distance = int(input_value)
        break
    else:
        print("Ошибка ввода: попробуйте еще раз.")

while True:
    input_value = input("Укажите дистанцию пробежки к которой Вы стремитесь (км): ")
    if isfloat(input_value):
        target_distance = int(input_value)
        break
    else:
        print("Ошибка ввода: попробуйте еще раз.")

while target_distance >= start_distance:
    print(f' {days_counter}-й день: {start_distance:.2f}')
    start_distance += (start_distance / 100) * 10
    days_counter += 1

start_distance += (start_distance / 100) * 10
print(
    f'\nОтвет: на {days_counter}-й день дистанция составит {start_distance:.2f}, '
    f'спортсмен достигнет результата — не менее {target_distance} км')

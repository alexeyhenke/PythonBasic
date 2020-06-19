"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
   но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

   Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
   Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
   но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
"""
import re

print("= " * 50)
print("{greeting:^100}".format(greeting="Добро пожаловать на страницу приложения выполняющую операции со строками!"))
print("= " * 50)

meta_symbol = ['!', '@', '#', '$', '%', '^', '&', '~']
iscontinue = True


def upper_first_leter(in_string: str):
    return in_string.title()


def check_latin_letter(in_str: str) -> int:
    pattern = r"[а-яА-Я]+"
    r = re.compile(pattern)
    ru_symbols = [w for w in filter(r.match, in_str)]
    return len(ru_symbols)


while iscontinue:
    res_str = ""
    input_str = input(f"Введите слово или строку из маленьких латинских букв (для завершения любой спецсимвол)\n{meta_symbol}: ")
    for n in input_str.split():
        if n in meta_symbol:
            iscontinue = False
            print(f'В строке был найден спец.символ "{n}". Программа завершается.')
            break

    if iscontinue:
        if input_str != "":
            if check_latin_letter(input_str) == 0:
                res_str = upper_first_leter(input_str)
                print("- " * 50)
                print(f'Исходное слово "{input_str}": Измененное слово "{res_str}"')
                print("- " * 50)
            else:
                print("Ошибка ввода: найдены кириллические символы")
        else:
            print("Ошибка ввода: поле ввода обязательно для заполнения")

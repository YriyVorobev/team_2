# Задача 1 (Создание и вызов функций)
# Напиши функцию print_hello(), которая выводит в консоль "Hello!" и ничего не возвращает (без return).
# Условия:
# Функция должна быть вызвана один раз после определения.
# Не используй аргументы.
from curses.ascii import isupper



def print_hello():
    print("Hello!")

print_hello()


# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая:
# Принимает два числа a и b
# Возвращает их произведение (не выводит!)
# Вызови функцию с аргументами 3 и 5 и выведи результат

def multiply(a, b):
    return a * b


result = multiply(3,5)
print(result)

# адача 3 (Аргументы с дефолтными значениями)
# Напиши функцию greet(name, greeting="Привет"), которая:
# Принимает имя (name) и приветствие (greeting), но greeting по умолчанию равно "Привет"
# Возвращает строку в формате: "[greeting], [name]!"
# Вызови функцию дважды:
# С одним аргументом: greet("Анна") → Должно вернуть "Привет, Анна!"
# С двумя аргументами: greet("Иван", "Здравствуй") → "Здравствуй, Иван!"
# Условия:
# Не используй print внутри функции, только return
# Дефолтное значение должно работать при вызове с одним аргументом

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

my_func = greet("Анна")
my_func2 = greet(greeting="Здравствуй",name="Иван")
print(my_func)
print(my_func2)

# Задача 4 (Возврат данных из функций)
# Напиши функцию is_positive(number), которая:
# Принимает число (number)
# Возвращает True, если число положительное, и False — если отрицательное или ноль
# Не используй print внутри функции
# Условия:
# Функция должна работать с целыми и дробными числами
# Выведи результат для чисел: 5, -3, 0


def is_positive(number):
    return number > 0


result = is_positive(5)
result2 = is_positive(-3)
result3 = is_positive(0)
print(result)
print(result2)
print(result3)


# Задача 5 (Декораторы)
# Напиши декоратор @repeat(n), который:
# Принимает аргумент n (сколько раз повторить вызов функции)
# Вызывает декорированную функцию n раз
# Возвращает результат последнего вызова
# Условия:
# Декоратор должен работать с функциями, которые возвращают значения
# Выведи результат для примера:


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    return f"Hello, {name}"


greet("Alice")


# Задача 7 (Декоратор с логированием)
# Напиши декоратор @log_call, который:
# Печатает "Функция вызвана" перед вызовом функции
# Вызывает исходную функцию
# Печатает "Функция завершила работу" после вызова
# Не изменяет возвращаемое значение функции

def my_log(func):
    def wrapper(*args, **kwargs):
        print("Функция вызвана")
        result = func(*args, **kwargs)
        print("Функция завершила работу")
        return result
    return wrapper

@my_log
def sum_numbers(a, b):
    return a + b
result = sum_numbers(2, 5)
print(result)


# (Функции в Python)
# Напиши функцию greet_user(), которая принимает имя пользователя (строка) и выводит сообщение:
# "Привет, [имя]! Добро пожаловать!".
# Вызови функцию с произвольным именем для проверки.

def greet_user(name):
    return f"Привет, {name}! Добро пожаловать!"

user = greet_user("Юрий")
print(user)

# (Аргументы функций)
# Напиши функцию multiply_numbers, которая принимает
# два числа и возвращает их произведение.
# Если передано только одно число, функция должна умножать его на 10.
# Пример вызова:
# multiply_numbers(3, 5) → 15
# multiply_numbers(4) → 40

def multiply_numbers(num1,num2=10):
    return num1 * num2

number3 = multiply_numbers(5,3)
number1 = multiply_numbers(3)
print(number1)
print(number3)

# (Возвращение данных из функций)
# Напиши функцию is_even,
# которая принимает число и возвращает True, если оно чётное, и False — если нечётное.
# Пример вызова:
# is_even(4) → True
# is_even(7) → False

def is_even(num):
    return num % 2 == 0

num1 = is_even(4)
print(num1)

# Декораторы)
# Напиши декоратор uppercase_decorator, который преобразует результат функции к верхнему регистру.

def upper(func):
    def wrapper(*args, **kwargs):
        print("Функция вызвана")
        result = func(*args, **kwargs)
        print("Функция завершена")
        return result.upper()
    return wrapper


@upper
def say_hello():
    return "hello"
print(say_hello())

# (Аргументы с дефолтными значениями)
# Напиши функцию create_user, которая принимает:
# Обязательный параметр username (строка)
# Необязательный параметр is_admin (по умолчанию False)
# Необязательный параметр access_level (по умолчанию 1)
# Функция должна возвращать словарь с этими параметрами.


def create_user(username, is_admin=False,access_level=1):
        resultr = {
            "username": username,
                   "is_admin":is_admin,
                   "access_level":access_level
        }
        return resultr


user_name = create_user("Alice")
print(user_name)


#  (Комбинированная)
# Напиши функцию calculate, которая:
# Принимает два числа и строку-операцию ('+', '-', '*', '/')
# По умолчанию операция должна быть '+'
# Возвращает результат операции или None, если операция неизвестна
# При делении на 0 возвращает "Ошибка: деление на ноль"


def calculator(num1, num2, operation='+'):
   if operation == "+":
      return num1 + num2
   elif operation == "-":
       return num1 - num2
   elif operation == "*":
       return num1 * num2
   elif operation == "/":
       if num2 == 0 :
         return "Делить на ноль нельзя"
       return num1 // num2
   else:
       return None

calculator_user = calculator(10,0,"/")
print(calculator_user)


# Задача 7 (Комбинированная: функции + условия)
# Напиши функцию check_temperature, которая:
# Принимает число (температуру) и строку unit (единицы измерения: 'C' или 'F', по умолчанию 'C')
# Возвращает:
# "Жарко" если температура >= 30°C или >= 86°F
# "Комфортно" если между 15°C и 30°C (или между 59°F и 86°F)
# "Холодно" если ниже 15°C (или 59°F)
# Если передан неизвестный unit (не 'C'/'F'), возвращает "Неизвестная единица измерения".

def check_temperature(temperature,measurements="C"):
    if measurements != "C" and measurements != "F":
        return "Неизвестная единица измерения"
    elif temperature >= 30 and measurements == "C" or temperature >=86 and measurements == "F":
        return "Жарко"
    elif (15< temperature < 30 and measurements == "C") or (59 < temperature < 86 and measurements == "F"):
        return "Комфортно"

    else:
        return "Холодно"
temper = check_temperature(50,"K")
print(temper)

# Задача 8 (Декораторы + аргументы)
# Напиши декоратор repeat_call, который:
# Принимает параметр n (количество повторений)
# Делает n вызовов декорируемой функции
# Возвращает список результатов всех вызовов
# Требования:
# Функция может принимать любые аргументы (*args, **kwargs)
# Если n <= 0, возвращает пустой список

def repeat_call(n):
    def decorator(func):
         def wrapper(*args, **kwargs):
          result =[]
          for _ in range(n):
             result.append(func(*args,**kwargs))
          return result
         return wrapper
    return decorator

@repeat_call(n=5)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


# Задача 9 (Функции + работа с данными)
# Напиши функцию process_text, которая:
# Принимает строку текста
# Возвращает словарь со статистикой:
# "words" — количество слов (разделены пробелами)
# "length" — общее количество символов
# "uppercase" — количество заглавных букв
# "digits" — количество цифр в тексте
# Пример:
# python
# text = "Hello World 2023!"
# print(process_text(text))
# Вывод:
# python
# {'words': 3, 'length': 15, 'uppercase': 2, 'digits': 4}
# Подсказки (если нужны):

def process_text(text):
    words = text.split()
    length = len(text)
    word = len(words)
    uppercase = 0
    digits = 0
    for chars in text:
        if chars.isupper():
            uppercase += 1
        if chars.isdigit():
            digits += 1
    return {
            "words": word,
            "length": length,
            "uppercase": uppercase,
            "digits": digits
        }


text1 = process_text("Hello words 2025 happy new year!!!!")
print(text1)


# Задача 10 (Простая функция с числами)
# Напиши функцию sum_and_check, которая:
# Принимает два числа
# Возвращает словарь с двумя значениями:
# "sum" — сумма этих чисел
# "is_even" — True, если сумма чётная, и False, если нет

def sum_and_check(num1, num2):
    """В общем решение хорошее, но можно лучше по словам дипсика!
    """
    result = num1 + num2
    if result % 2 == 0:
        is_even = True
    else:
        is_even = False
    return {"sum": result, "is_even": is_even}

sum_and_checks = sum_and_check(2,2)
print(sum_and_checks)

def sum_and_check1(num1, num2, num3=0):
    """Хорошее решение, с подсказами дипсика"""
    result = num1 + num2 + num3
    return {"sum": result, "is_even": result %2 == 0}

suma = sum_and_check1(2,5,7)
print(suma)

# Задача 11 (Списки + функции)
# Напиши функцию process_list, которая:
# Принимает список чисел
# Возвращает новый список, где:
# Каждое чётное число умножено на 2
# Каждое нечётное число оставлено как есть
# Пример:
# python
# print(process_list([1, 2, 3, 4]))  # [1, 4, 3, 8]
# Подсказки (если нужны):
# Создай новый пустой список (result = [])
# Перебери исходный список циклом for
# Для проверки чётности используй % 2 == 0
# Добавляй обработанные числа в новый список (result.append())

def process_list(numbers):
    result = []
    for number in numbers:
        if number %2 == 0:
            result.append(number*2)
        else:
            result.append(number)
    return result


process = process_list([2,3,4])
print(process)


# Задача 12 (Питоновский стиль: списки + строки)
# Напиши функцию format_emails, которая:
# Принимает список email-адресов (например, ["user1@test.com", "user2@example.org"])
# Возвращает новый список, где:
# Домены (часть после @) заменены на "company.com"
# Сами логины (часть до @) остаются без изменений
# Требования:
# Решить в одну строку (через list comprehension)
# Использовать split() или replace()


def format_emails(list1):
    return [email.split("@")[0] + "@company.com" for email in list1]

format = format_emails(["user1@test.com", "user2@example.org"])
print(format)


# Задача 13 (Списки + условия)
# Напиши функцию get_short_words, которая:
# Принимает список слов (например, ["apple", "banana", "pear", "kiwi"])
# Возвращает новый список, где:
# Остаются только слова короче 5 букв
# Все выбранные слова переводятся в верхний регистр
# Пример вызова:
# python
# words = ["apple", "banana", "pear", "kiwi"]
# print(get_short_words(words))
# Ожидаемый вывод:
# python
# ['PEAR', 'KIWI']  # "apple" (5 букв) и "banana" (6 букв) не подходят

def get_short_words(lst):
    result = []
    for word in lst:
        if len(word) < 5:
            result.append(word.upper())
    return result

get_short = get_short_words(["apple", "banana", "pear", "kiwi"])
print(get_short)

def get_shorts(lst1):
    return [word.upper() for word in lst1 if len(word) < 5]
print(get_shorts(["apple", "banana", "pear", "kiwi"]))


# Задача 15 (Списки + строки)
# Напиши функцию count_vowels, которая:
# Принимает строку (например, "Hello World")
# Возвращает количество гласных букв (a, e, i, o, u) в этой строке
# Считаются буквы в любом регистре (A и a — одинаково)
# Пробелы и другие символы игнорируются

def count_vowels(vowel):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count_vowel = []
    for wov in vowel:
        repeat = wov.lower()
        if repeat in vowels:
            count_vowel.append(repeat)
    return count_vowel


count_vowels = count_vowels("Hello word! my name is Yuriy")
print(count_vowels)






import json
from json.decoder import JSONDecodeError

from PythonLessons.lessons_8 import upper

# Задача 3 — Списки
# Дан список:
nums = [5, 0, -3, 8, 5, -3, 10]
# Нужно:
# Удалить из списка все отрицательные числа.
# Убрать дубликаты.
# Отсортировать список по возрастанию.
# И вывести итоговый результат.

list_comprehension = [x for x in nums if x >= 0]
num = sorted(list(set(list_comprehension)))
print(num)

# Задача 4 — Условные операторы
# Дано число n.
# Нужно написать проверку:
# если n делится на 3 → вывести "Fizz",
# если делится на 5 → вывести "Buzz",
# если делится и на 3, и на 5 → вывести "FizzBuzz",
# иначе → вывести само число.

n = 15

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 ==0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)


# Задача 5 — Словари
# Дан словарь с данными о пользователе:
user = {
    "name": "Алексей",
    "age": 25,
    "city": "Москва"
}
# Нужно:
# Увеличить возраст на 1.
# Добавить новый ключ "email" с любым значением.
# Удалить ключ "city".
# Вывести итоговый словарь.

user["email"] = "name@example.com"
del user["city"]
user["age"] +=1

print(user)

# адача 6 — Циклы
# Нужно вывести все числа от 1 до 30,
# но пропускать числа, которые делятся на 7.

for i in range(1,31):
    if i % 7 == 0:
        continue
    print(i)

i = 1
while i <= 30:
    if i % 7 == 0:
        i += 1
        continue
    print(i)
    i +=1

# Задача 7 — Циклы с continue
# Выведи все числа от 1 до 50,
# но пропусти:
# те, что делятся на 4,
# и те, что делятся на 9.


for i in range(1,51):
    if i % 4 == 0 or i % 9 == 0:
        continue
    print(i)

i = 1
while i <= 50:
    if i % 4 == 0 or i % 9 ==0:
        i += 1
        continue
    print(i)
    i += 1


# Задача 8 — Файлы
# Создай файл numbers.txt и запиши в него числа от 1 до 20, каждое с новой строки.
# Потом открой этот файл для чтения.
# Выведи на экран только те строки, где число чётное.

with open("numbers.txt", "w") as file:
    lines = [str(i) + "\n" for i in range(1,21)]
    file.writelines(lines)

with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        num = int(i.strip())
        if num % 2 ==0:
            print(num)

# Задача 9 — Функции
# Напиши функцию square_or_double(n), которая:
# если число чётное → возвращает его квадрат,
# если нечётное → возвращает удвоенное значение.


def square_or_double(n):
    if n % 2 == 0:
       return n ** 2
    else:
        return n * 2

print(square_or_double(4))


# адача 10 — Функции с параметрами
# Напиши функцию compare_numbers(a, b), которая:
# если a > b → возвращает строку "Первое число больше",
# если a < b → возвращает строку "Второе число больше",
# если равны → возвращает строку "Числа равны".
# 📌 Подсказка: тут нужно 3 ветки условий — if, elif, else.

def compare_numbers(a, b):
    if a > b:
        return f"Первое число больше"
    elif a < b:
        return f"Второе число больше"
    else:
        return f"Числа равны"
print(compare_numbers(2,5))


# Задача 11 — ООП (часть 1)
# Создай класс Book, у которого есть два атрибута:
# title (название книги),
# author (автор книги).
# Задачи:
# Сделай так, чтобы при создании объекта эти значения задавались через конструктор (__init__).
# Создай объект с любыми значениями.
# Выведи на экран название и автора этой книги.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"


book = Book("Моряк и море", "Сардельки")
print(book)

# Задача 12 — ООП (часть 2)
# Создай класс Dog, у которого:
# есть атрибуты name (кличка) и age (возраст), задаются через __init__,
# есть метод bark(), который выводит строку "Гав-гав! Меня зовут {name}",
# есть метод get_age_in_human_years(),
# который возвращает возраст собаки в «человеческих годах» (возьми условно: 1 год собаки = 7 лет человека).

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age =age

    def bark(self):
        return f"Гав-гав! Меня зовут {self.name}"

    def get_age_in_human_years(self):
        return f"Возраст собаки в человеческих годах {self.age * 7}"

dog = Dog("Ротик", 15)
print(dog.bark())
print(dog.get_age_in_human_years())


# 🔹 Задача 13 — ООП (наследование)
# Создай два класса:
# Базовый класс Animal
# атрибут name (имя животного),
# метод sleep() → выводит строку "Животное {name} спит".
# Дочерний класс Cat, который наследуется от Animal:
# имеет дополнительный метод meow() → выводит строку "Кот {name} говорит: Мяу!".
# Задачи:
# Создай объект кота с именем.
# Вызови у него метод sleep() из родительского класса.
# Вызови метод meow() из дочернего класса.


class Animal:

    def __init__(self,name,):
        self.name = name

    def sleep(self):
        return f"Животное {self.name} спит"

class Cat(Animal):

     def __init__(self,name):
         super().__init__(name)

     def meow(self):
         return f"Кот {self.name} говорит: Мяу!"

animal = Animal("Karry")
print(animal.name)
print(animal.sleep())

cat = Cat("Karry")
print(cat.sleep())
print(cat.meow())


# Задача 14 — Обработка исключений
# Напиши программу, которая:
# Просит у пользователя ввести число (через input).
# Преобразует ввод в int.
# Если пользователь ввёл не число → программа не падает,
# а выводит сообщение "Ошибка: нужно ввести целое число!".


# try:
#     integer = int(input("введи число: "))
#
# except ValueError:
#     print(" Это не число , Введи число!")
#
# else:
#     print(integer)

# Задача 15 — Файлы + обработка ошибок
# Напиши программу, которая:
# Пытается открыть файл с именем data.txt для чтения.
# Если файла нет → не падает, а выводит сообщение "Файл не найден!".
# Если файл есть → читает содержимое и печатает его на экран.
# Подсказка: здесь в try пойдёт open("data.txt", "r"), а в except нужно поймать исключение FileNotFoundError.
# Хочешь, я намекну, как использовать with open(...) внутри try, чтобы корректно закрывался файл?

# try:
#     with open("data.txt", "r") as file:
#         line = file.read()
#         print(line)
# except FileNotFoundError:
#     print("Файл не найден, создай его!")
#
#
#
# with open("json.json", "r") as file:
#     data = json.load(file)
#     for i in data:
#         if i.get("age") and i.get("email"):
#             if i.get("age") >= 18:
#                 print(i.get("email"))


# Задача:
# У тебя есть список словарей с данными о товарах в магазине:
products = [
    {"name": "Laptop", "price": 1200, "quantity": 4},
    {"name": "Phone", "price": 800, "quantity": 10},
    {"name": "Keyboard", "price": 50, "quantity": 0},
    {"name": "Monitor", "price": 300, "quantity": 5},
    {"name": "Mouse", "price": 25, "quantity": 20},
]
# Требуется:
# Отобрать только те товары, у которых quantity > 0.
# Отсортировать их по цене (от дешёвых к дорогим).
# Вывести названия товаров в таком порядке.
sorted_products = sorted(products,key=lambda x:x["price"])
for i in sorted_products:
    if i["quantity"] > 0:
        print(i)


# Задача 1: Анализ строки
# Условие:
# Напишите программу, которая запрашивает у пользователя любую строку и затем:
# Выводит ее длину.
# Переводит ее в верхний регистр.
# Определяет, является ли она палиндромом (
# читается одинаково слева направо и справа налево,
# например, "анна").
# Регистр букв не должен учитываться.
# Программа должна вывести True или False.
#
# string_string = input()
# len_string = len(string_string)
# upper_string = string_string.upper()
# polindrom = string_string.lower() == string_string[::-1].lower()
# print(string_string)
# print(len_string)
# print(upper_string)
# print(polindrom)


# Задача 2 (Актуальная): Фильтрация списка чисел
# Условие:
# У вас есть готовый список чисел (данные, которые могли бы прийти из другого источника, например, из файла или от системы):
numbers = [15, 62, 84, 33, 71, 90, 22, 48, 97, 3, 66, 101, 28, 55, 77, 12, 39, 88, 51, 24]
# Ваша задача:
# Создать новый список, который будет содержать только те числа из исходного списка, которые:
# Больше 50.
# И являются четными.
# Выведите оба списка: исходный и новый.
# Цель: Отработка цикла for, условного оператора if и логического оператора and на реальных данных.
# Подсказка (если нужно):
# Вам не нужно генерировать список, он уже дан. Проинициализируйте переменную numbers этим списком.
# Ваша главная задача — пройтись по нему циклом и применить условия фильтрации.

listed_numbers = []
for i in numbers:
    if i > 50 and i %2 == 0:
        listed_numbers.append(i)


print(listed_numbers)
print(numbers)

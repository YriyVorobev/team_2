# Задача 1 — Строки и методы
# Создай переменную со строкой твоего имени.
# Преобразуй строку к верхнему регистру.
# Замени в строке одну букву на другую (на твой выбор).
# Выведи длину строки.
# Когда будешь готов — пришли своё решение. Если понадобится, дам короткие подсказки, что поправить.
from fileinput import filename

from lessons_4 import balance, username

name = "Юрий"
print(name)

upper_name = name.upper()
print(upper_name)

name_replace = name.replace("Ю","Р",1)
print(name_replace)

name_len = len(name)
print(name_len)


# Задача 2 — Срезы строк
# Создай строку со словом: автоматизация.
# Выведи первые 5 символов.
# Выведи последние 3 символа.
# Выведи каждый второй символ (начиная с первого).
# Разверни строку и выведи результат.

automation = "Автоматизация"

automation_first_five = automation[:5]
print(automation_first_five)

automation_last_three = automation[-3:]
print(automation_last_three)

automation_step2 = automation[0::2]
print(automation_step2)

automation_reversed = automation[::-1]
print(automation_reversed)


# Задача 3 — Срезы и методы
# Создай строку: Программирование.
# Выведи первые 4 символа.
# Выведи последние 4 символа.
# Выведи каждый третий символ, начиная с первого.
# Преобразуй строку в нижний регистр и разверни её.


programs = "Программирование"

programs_first_four = programs[:4]
print(programs_first_four)

programs_last_four = programs[-4:]
print(programs_last_four)

programs_step_three = programs[::3]
print(programs_step_three)

programs_lower_reversed = programs.lower()[::-1]
print(programs_lower_reversed)


# Задача 4 — Строки: поиск и подсчёт
# Создай строку: автотестирование.
# Проверь, содержит ли строка подстроку "тест" и выведи результат (булево).
# Найди индекс первого вхождения подстроки "то".
# Подсчитай количество букв "о" в строке.
# Замени только первое вхождение "то" на "ТО" и выведи результат.


autotest = "автотестирование"

autotest_bool = "тест" in "автотестирование"
print(autotest_bool)

autotest_find = autotest.find("то")
print(autotest_find)

autotest_count = autotest.count("о")
print(autotest_count)

autotest_replace = autotest.replace("то","ТО",1)
print(autotest_replace)


# Задача 5 — Строки: split/strip/join
# Создай строку: " python,java, golang , c++ "
# Разбей строку по запятой на элементы.
# Удали пробелы по краям у каждого элемента.
# Собери обратно строку, соединив элементы через точку с запятой.
# Выведи количество языков и итоговую строку.

language = " python,java, golang , c++ "

language_del = language.strip("")
print(language_del)

language_split = language_del.split(",")
print(language_split)

clean = list(map(str.strip, language_split))
print(clean)

join_language = ";".join(clean)
print(join_language)

len_language = len(clean)
print(len_language)

# Задача 6 — Строки: префиксы/суффиксы и пробелы
# Создай строку: " test automation course "
# Удали пробелы по краям.
# Проверь, начинается ли строка с "test" без учёта регистра (выведи булево).
# Проверь, заканчивается ли строка на "course" (выведи булево).
# Замени все последовательности пробелов внутри на один пробел.
# Преобразуй строку к виду, где каждое слово начинается с заглавной буквы.

test = " test automation course "

test_strip = test.strip()
print(test_strip)

test_start_with = test_strip.startswith("test")
print(test_start_with)

test_end_with =test_strip.endswith("course")
print(test_end_with)

test_title =test_strip.title()
print(test_title)

test_normalized = " ".join(test.split())
print(test_normalized)


# Задача 7 — Строки и форматирование
# Создай переменные: имя (строка) и возраст (число).
# Собери фразу: “Меня зовут [имя], мне [возраст]”.
# Увеличь возраст на 1 и выведи обновлённую фразу.
# Если будешь приводить возраст к строке — выведи тип переменной до и после.


name = "Юрий"
age = 18
print(f"Меня зовут {name}, мне {age}")

age += 1
print(f"Меня зовут {name}, мне {age}")


# Задача 8 — Преобразование типов и сравнение
# Создай переменные: a = "10" (строка) и b = 5 (число).
# Преобразуй a к числу и сложи с b; выведи результат.
# Сравни сумму с 15; выведи булево.
# Преобразуй сумму к строке; выведи тип до и после преобразования.
# Дополнительно: поменяй b на строку "5" и попробуй сложить без приведения — объясни, что произойдёт и почему.

a = "10"
b = 5
a = int(a)

c = a + b
print(c)

comparison = c == 15
print(comparison)

print(type(c))

transformation = str(c)
print(type(transformation))

# d = str(b)
# summa = a + d
# print(summa)
# Да, объяснил правильно: Python не приводит str и int автоматически
# — при сложении будет TypeError. Если оба строки
# — конкатенация, если оба числа — сложение 1. Готов к следующей задаче?


# Задача 9 — Списки (база)
# Создай список из трёх языков программирования.
# Выведи первый и последний элемент.
# Замени второй элемент на другой.
# Добавь новый язык в конец списка.
# Удали первый элемент (по индексу или по значению).
# Выведи длину списка.

language_list = ["Python", "C++", "Java"]
print(language_list[0], language_list[-1])

language_list[1] = "Golang"
print(language_list)

language_list.append("C#")
print(language_list)

del language_list[0]
print(language_list)

print(len(language_list))


# Задача 10 — Списки: insert/remove/in
# Создай список чисел: 3, 1, 4.
# Вставь число 2 на позицию 1.
# Удали из списка число 4.
# Добавь в конец число 5.
# Проверь, есть ли число 3 в списке, выведи результат (булево).
# Выведи итоговый список и его длину.

num_list = [3, 1, 4]
num_list.insert(1, 2)
num_list.remove(4)
num_list.append(5)
num_list_bool = 3 in num_list

print(num_list_bool)
print(num_list)
print(len(num_list))

# Задача 11 — Списки: срезы и удаление
# 1) Создай список: [10, 20, 30, 40, 50].
# 2) Выведи первые 3 элемента (срез).
# 3) Выведи последние 2 элемента (срез).
# 4) Удали последний элемент методом удаления и сохрани его в переменную.
# 5) Выведи сохранённое значение и итоговый список.


list_num = [10, 20, 30, 40, 50]
print(list_num[:3])
print(list_num[-2:])
list_num_pop = list_num.pop()
print(list_num_pop)
print(list_num)


# Задача 1
# Тема: Срезы
# Условие: Есть строка: Python. Получи подстроку yth с помощью среза и выведи результат.

python_string = "Python"
string_3_symbol = python_string[1:4]
print(string_3_symbol)


# Задача 2
# Тема: F-строки
# Условие: Дано имя Иван и возраст 25. Выведи строку: Меня зовут Иван, мне 25 лет — используя f-строку.

name = "Иван"
age = 25
print(f"Меня зовут {name}, мне {age} лет")


# Задача 3
# Тема: Конкатенация строк
# Условие: Даны строки s1 = "Привет" и s2 = "мир". Собери строку
# "Привет мир" с помощью конкатенации (+) и выведи результат.

s1 = "Привет"
s2 = "мир"
s3 = s1 + " " + s2
print(s3)

# Задача 4
# Тема: Доступ к символам
# Условие: Дана строка: s = "Python". Выведи первый символ и последний символ на отдельных строках.

s = "Python"
one_symbol = s[0]
print(one_symbol)
the_end_symbol = s[-1]
print(the_end_symbol)

# Задача 5
# Тема: Длина строки
# Условие: Дана строка s = "Привет!". Выведи её длину.

s = "Привет!"
print(len(s))


# Задача 6
# Тема: Создание строки
# Условие: Создай строку s со значением Привет, Python! и выведи её.

s = "Привет, Python!"
print(s)

# Задача 7
# Тема: Базовые методы строк
# Условие: Дана строка: s = "python". Выведи эту строку в верхнем регистре.

s = "python"
print(s.upper())

# Задача 8
# Тема: Базовые методы строк
# Условие: Дана строка: s = " Привет, мир! ". Удали пробелы по краям и выведи результат.

s = " Привет, мир! "
print(s.strip())

# Задача 9
# Тема: Базовые методы строк
# Условие: Дана строка: s = "Привет, мир!". Замени слово "мир" на "Python" и выведи результат.

s = "Привет, мир!"
w = s.replace("мир","Python")
print(w)

# Задача 10
# Тема: Срезы
# Условие: Дана строка s = "Python". Получи подстроку "Pto" с помощью среза с шагом 2 и выведи результат.

s = "Python"
print(s[:-1:2])

# Задача 11
# Тема: Базовые методы строк
# Условие: Дана строка: s = "Python". Проверь, начинается ли она с "Py", и выведи результат (True/False).

s = "Python"
e = "Py" in s
print(e)

# Задача 12
# Тема: Доступ к символам
# Условие: Дана строка s = "Python". Выведи третий символ строки.

s = "Python"
print(s[2])

# Задача 1
# Тема: Добавление элементов в конкретное место списка
# Условие: Дан список nums = [1, 2, 4]. Вставь число 3 так, чтобы получился [1, 2, 3, 4], и выведи список.

nums = [1, 2, 4]
nums.insert(2,3)
print(nums)

# Задача 2
# Тема: Удаление элементов из списка
# Условие: Дан список nums = [1, 2, 3, 4]. Удали элемент 3 по значению и выведи список.

nums = [1, 2, 3, 4]
nums.remove(3)
print(nums)

# Задача 3
# Тема: Слияние списков
# Условие: Даны списки a = [1, 2] и b = [3, 4].
# Получи список [1, 2, 3, 4] с помощью слияния и выведи результат.

a = [1, 2]
b = [3, 4]
list_merger = a + b
print(list_merger)


# Задача 4
# Тема: Срезы списка
# Условие: Дан список nums = [10, 20, 30, 40, 50].
# Получи подсписок [20, 30, 40] с помощью среза и выведи результат.

nums = [10, 20, 30, 40, 50]
p = nums[1:4:]
print(p)

# Задача 5
# Тема: Замена элементов в списке
# Условие: Дан список nums = [1, 2, 3].
# Замени второй элемент на 20 и выведи список.

nums = [1, 2, 3]
nums[1] = 20
print(nums)

# Задача 6
# Тема: Добавление элементов в список
# Условие: Дан список fruits = ["яблоко"].
# Добавь в конец "банан" и выведи список.

fruits = ["яблоко"]
fruits.append("банан")
print(fruits)

# Задача 7
# Тема: Очистка списка
# Условие: Дан список nums = [1, 2, 3].
# Очисти список и выведи результат.

nums = [1, 2, 3]
nums.clear()
print(nums)

# Задача 8
# Тема: Получение элементов списка
# Условие: Дан список colors = ["red", "green", "blue"]. Выведи второй элемент списка.

colors = ["red", "green", "blue"]
print(colors[1])

# Задача 9
# Тема: Удаление элементов из списка
# Условие: Дан список nums = [10, 20, 30, 40].
# Удали элемент по индексу 2 и выведи список.

nums = [10, 20, 30, 40]
nums.pop(2)
print(nums)

# Задача 10
# Тема: Срезы списка
# Условие: Дан список nums = [1, 2, 3, 4, 5, 6].
# Получи подсписок [1, 3, 5] с помощью среза с шагом и выведи результат.

nums = [1, 2, 3, 4, 5, 6]
print(nums[::2])

# Задача 1
# Тема: Оператор if
# Условие: Дан num = 5. Если число больше 0, выведи "положительное".

num = 5
if num > 0:
    print("положительное")

# Задача 2
# Тема: Тернарный оператор
# Условие: Дан num = -3.
# С помощью тернарного оператора выведи "положительное", если num > 0, иначе — "неположительное".

num1 = -3
result = "положительное" if num1 > 0 else "неположительное"
print(result)

# Задача 1. Переменные и типы данных
#
# 1. Создайте переменную `number` со значением 42.
# 2. Преобразуйте её в строку и сохраните в переменную `number_str`.
# 3. Создайте переменную `text` со значением "The answer is: ".
# 4. Объедините строку `text` и строку `number_str` и сохраните результат в переменную `result`.
#
# 5. Выведите на экран:
#
# - значение и тип данных `number`,
# - значение и тип данных `number_str`,
# - значение и тип данных `text`,
# - значение и тип данных `result`.

number = 42
number_str = str(number)

text = "The answer is: "
result = text + number_str

print(number, type(number))
print(number_str, type(number_str))
print(text, type(text))
print(result)
# ==========================================
#
# # Задача 2. Строки
# #
# # Даны две переменные:
# #
# # name = "внесите ваше имя сюда"
# # age = введите ваш возраст.
# #
# # Используя f-строку, выведите на экран сообщение: "Меня зовут ваше имя, мне ваш возраст лет."

name = "Юрий"
age = 30
print(f"Меня зовут {name}, мне {age} лет.")


#===========================================

#Задача 3. Списки
#Дан список my_list = [1, 2, 3].
#Создайте копию этого списка, измените первый элемент копии на #10 и выведите оба списка.

my_list = [1, 2, 3]
copy = my_list.copy()
copy[0] = 10
print(my_list)
print(copy)


#==========================================
#Задача 4. Условные операторы
#Напишите программу, которая принимает число от пользователя и #проверяет:
# Если число больше 0, выведите "Положительное".
# Если число равно 0, выведите "Ноль".
# Если число меньше 0, выведите "Отрицательное".
numbers = 3

if numbers > 0:
    print("Положительное")
elif numbers == 0:
    print("Ноль")
else:
    print("Отрицательное")

#=============================================
#Задача 5. Словари
#Дан словарь:
person = {

    "name": {

        "first_name": "Иван",
        "last_name": "Иванов"

    },

    "address": {

        "city": "Москва",
        "country": "Россия"

    }

}
#Обновите значение ключа "city" на "Ставрополь" и добавьте #новый ключ "postal_code" со значением "333777" в словарь #"address".
#Выведите значение через print.
#Затем удалите ключ "city" из вложенного словаря "address" и #снова выведите значение через print.

person["address"]["city"] = "Ставрополь"
person["address"]["postal_code"] = "333777"
print(person)
del person["address"]["city"]
print(person)
#=============================================

#Задача 6. Циклы
#Напишите цикл while, который выводит числа от 1 до 20, но
#пропускает числа, которые делятся на 4 (используйте continue)

i = 1
while i <= 20:
    if i % 4 == 0:
        i += 1
        continue
    print(i)
    i += 1

# =============================================

# Задача 7. Файлы
# Создайте файл с именем "fruits.txt" и запишите в него названия #фруктов:
# "яблоко", "банан", "апельсин" (каждое с новой строки).
# Затем откройте этот файл, прочитайте все строки и выведите на #экран только те строки, которые начинаются с буквы "а".


with open("fruits.txt", "w") as file:
    file.write("яблоко,\nбанан,\nапельсин")

with open("fruits.txt", "r") as file:
    fruit = file.readlines()
    for fruits in fruit:
        if fruits.strip().startswith("а"):
            print(fruits)




# ===========================================
    # Задача 8. Функции
    # Напишите функцию greet_user, которая приветствует пользователя #в зависимости от его роли и имени. Функция должна принимать #два параметра:
    # user_role (обязательный) — строка, указывающая роль #пользователя (например, "Администратор", "Гость", "Модератор").
    # user_name (необязательный) — строка с именем пользователя. По #умолчанию должно быть None.
    # Логика работы функции:
    # Если имя пользователя передано
    # (user_name не None и не пустая строка),
    # то функция должна вывести:
    # "Привет, {user_name}! Ваша роль: {user_role}."
    # Если имя не передано (user_name равно None или пустая #строка), функция должна вывести: "Привет, Гость! Ваша роль: #{user_role}."

def great_user(user_role,user_name=None):
    if user_name:
        print(f"Привет, {user_name}! Ваша роль {user_role}")
    else:
        print(f"Привет, гость! Ваша роль {user_role}")
great_user("Админ", "Юрий")
great_user("Пользователь")

    # ===========================================

    # Задача 9. ООП ч.1
    # Создайте класс `Student`.
    # У класса должны быть атрибуты `name`  и `age`, которые #задаются при создании объекта через конструктор `__init__`.
    # Создай объект класса `Student` с вашим именем и вашим возрастом.
    # Выведи на экран имя и возраст студента.


class Student:
    def __init__(self,name1, age1):
        self.name = name1
        self.age = age1


students = Student("Юрий", 18)
print(students.name)
print(students.age)


    # == == == == == == == == == == == == == == == == == == == == == =

    # Задача 10. ООП ч.2
    # Создайте класс Animal с атрибутами:
    # name (кличка животного)
    # species (вид животного, например "собака")
    # И методами:
    # eat()
    # sleep()
    # Затем создайте дочерний класс Dog, который:
    # Наследует все от класса Animal
    # Имеет дополнительный метод bark() (лаять)
    # Задание:
    # Создайте объект my_dog класса Dog с любым именем
    # Вызовите все три метода eat(), sleep(), bark() и выведите #результаты



class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species


    def eat(self):
        return "ест"

    def sleep(self):
        return "спит"


class Dog(Animal):

    def bark(self):
        return "лаять"

my_dog = Dog("Шарик","Дворняга")

print(my_dog.bark())



# Задача 11. Парсинг и фильтрация данных
# У тебя есть список словарей — имитирует JSON-ответ от API. Каждый словарь содержит информацию о товаре:
# python
# Копировать
# Редактировать
products = [
    {"name": "Книга", "price": 450, "in_stock": True},
    {"name": "Ноутбук", "price": 75000, "in_stock": False},
    {"name": "Ручка", "price": 50, "in_stock": True},
    {"name": "Смартфон", "price": 50000, "in_stock": True},
]
# 🎯 Твоя задача:
# Получить только те товары, которые есть в наличии (in_stock == True).
# Из этих товаров выбрать те, у которых цена больше 1000.
# Вывести на экран названия этих товаров.

for product in products:
    if product["in_stock"]:
        if product["price"] > 1000:
            print(product["name"])


# Задача 12. Обработка ответов от API
# У тебя есть список словарей, каждый из которых представляет "результат запроса пользователя". Внутри есть имя, статус ответа, и код:

responses = [
    {"user": "Иван", "status": "success", "code": 200},
    {"user": "Мария", "status": "error", "code": 500},
    {"user": "Павел", "status": "success", "code": 201},
    {"user": "Анна", "status": "error", "code": 404},
]

# 🎯 Твоя задача:
# Найти все записи, где status — "error".
# Для этих записей вывести имя пользователя и код ошибки в формате:
# Пользователь: Анна — Код ошибки: 404

for response in responses:
    if response["status"] == "error":
        print(f"Пользователь: {response['user']} - Код ошибки: {response['code']}")




# Задача 13. Проверка корректности данных пользователей
# У тебя есть список пользователей:
users = [
    {"name": "Иван", "age": 25, "email": "ivan@example.com"},
    {"name": "Мария", "age": 17, "email": "masha[at]example.com"},
    {"name": "Павел", "age": 35, "email": "pavel@example.com"},
    {"name": "Алекс", "age": 16, "email": "alex@example"},
]
# 🎯 Твоя задача:
# Для каждого пользователя:
# Проверить, что его возраст от 18 и выше.
# Проверить, что его email содержит символ @ и точку ..
# Если оба условия соблюдены — вывести сообщение:
# Иван: данные корректны
# Иначе:
# Мария: данные некорректны

for user in users:
    if user["age"] >= 18:
        if "@" in user["email"] and "." in user["email"]:
            print(f"{user['name']}: данные корректны")
        else:
            print(f"{user['name']}: данные некорректны")

# Задача 14. Обработка вложенных данных
# У тебя есть список заказов. Каждый заказ — это словарь с данными пользователя и списком купленных товаров:

orders = [
    {
        "user": "Иван",
        "items": [
            {"name": "Книга", "price": 500},
            {"name": "Ручка", "price": 100}
        ]
    },
    {
        "user": "Мария",
        "items": [
            {"name": "Ноутбук", "price": 85000}
        ]
    },
    {
        "user": "Павел",
        "items": []
    }
]
# Твоя задача:
# Для каждого пользователя рассчитать общую сумму покупок.
# Если список покупок пустой — вывести "Нет покупок".
# Иначе вывести:
# Иван: сумма покупок — 600

for order in orders:
    if order['user'] and order['items']:
        total = 0
        for item in order['items']:
             total += item['price']
        print(f"{order['user']}: сумма покупок - {total}")

    else:
        print(f"{order['user']}: Нет покупок")

#
# 🔹 Задача 15. Валидация JSON-ответа
# Представь, что ты получил такой ответ от API (например, список пользователей):
response = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Мария"},
    {"id": 3, "name": "Павел", "email": "pavel@example.com"},
    {"id": 4, "email": "anna@example.com"},
]
# 🎯 Твоя задача:
# Для каждого объекта в списке:
# Проверить, что в словаре есть ключи:
# "id"
# "name"
# "email"
# Если какие-то из них отсутствуют — вывести:
# Ошибка в записи id: 2 — отсутствует ключ: email
# Или, если нет "id", то:
# Ошибка: запись без id — отсутствует ключ: name
# 🧠 Задача про:
# проверку ключей в словарях,
# вложенные условия,
# защиту от отсутствующего "id" при выводе.



for responses in response:
    if "id" in responses:
        user_id = responses["id"]
        if "name" not in responses:
            print(f"Ошибка в записи id: {user_id} — отсутствует ключ: name")
        if "email" not in responses:
            print(f"Ошибка в записи id: {user_id} — отсутствует ключ: email")

    else:
        if "name" not in responses:
            print("Ошибка: запись без id — отсутствует ключ: name")
        if "email" not in responses:
            print("Ошибка: запись без id — отсутствует ключ: email")



# Задача 17. Список заказов — фильтрация по количеству товаров
# У тебя есть список заказов, примерно такого вида:
orders = [
    {"id": 1, "user": "Иван", "items": ["товар1", "товар2"]},
    {"id": 2, "user": "Мария", "items": ["товар1"]},
    {"id": 3, "user": "Андрей", "items": ["товар1", "товар2", "товар3", "товар4"]},
    {"id": 4, "user": "Ольга", "items": []},
]
# 🎯 Твоя задача:
# 🔍 Вывести только тех пользователей, у которых в заказе более двух товаров
# (т.е. длина списка items больше 2)

for order in orders:
    if ("items" in order and
            type(order["items"]) == list
            and len(order["items"]) > 2):
        print(f"У пользователя с именем {order['user']} и id {order['id']} больше 2-х заказов")


# Задача 18. Классы — Банковский счёт
# Создай класс BankAccount, который будет моделировать банковский счёт.
# 🎯 Задание:
# У класса должен быть конструктор __init__, который принимает:
# имя владельца (owner)
# начальный баланс (balance, по умолчанию 0)
# Добавь методы:
# deposit(amount) — пополнение счёта на amount
# withdraw(amount) — снять со счёта сумму amount, но только если хватает средств
# get_balance() — возвращает текущий баланс
# Проверь работу: создай счёт, пополни, сними, выведи баланс.

class BankAccount:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
         self.balance += amount
         print(f"Баланс: {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Ваш баланс {self.balance}")
        else:
            self.balance -= amount
            print(f"Успешно снята сумма {amount}")

    def get_balance(self):
        return self.balance


bank = BankAccount("Юрий", 1000)
bank.deposit(100)
print(bank.get_balance())
bank.withdraw(300)
print(bank.get_balance())


# Создай базовый класс User с:
# username
# методом view_dashboard() — просто print("Просмотр панели")
# Создай класс Admin, который наследует User, и добавь:
# метод delete_user(username) — выводит: Пользователь {username} удалён
# Создай класс Guest, тоже наследник User, но:
# Переопредели view_dashboard() так, чтобы он выводил:
# "У гостя нет доступа к панели"


class User:

    def __init__(self,username):
        self.username = username


    def view_dashboard(self):
        print("Просмотр панели")


class Admin(User):

    def __init__(self,username):
        super().__init__(username)

    def delete_user(self,username):
        return f"Пользователь {username} удален"

class Guest(User):

    def __init__(self):
        super().__init__(username)

    def view_dashboard(self):
        print(f"У гостя нет доступа к панели")


user = User("Юрий")
user.view_dashboard()

admin = Admin("Админ")
print(admin.delete_user("Юрий"))

guest = Guest()
guest.view_dashboard()


# адача 20. Классы + Файлы — Сохранение пользователей
# Создай класс User, который умеет сохранять данные в файл и загружать их оттуда.
# 🎯 Задание:
# Класс User должен принимать:
# username
# email
# Добавь метод save_to_file(filename), который:
# сохраняет имя и email в файл построчно:
# пример: username,email
# Добавь метод @staticmethod load_users(filename), который:
# читает всех пользователей из файла и выводит в консоль
# пример:
# Загружен пользователь: username - email

class User:

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def save_to_file(self,filename):
        with open(filename, "w") as file:
            file.write(f"{self.username}, {self.email}\n")

    @staticmethod
    def load_users(filename):
        with open(filename, "r") as file:
                files = file.readlines()
                for line in files:
                    name, email = line.strip().split(",")
                    print(f"Загружен пользователь {name} - {email}")


user = User("Юрий", "Юрий@mail.com")
user.save_to_file("Nores")
User.load_users("Nores")


# Задача: "Фильтр уникальных и отсортированных значений"
# У тебя есть список с числами, в котором могут быть:
# Повторы
# Отрицательные числа
# Нули
# Пример входных данных:
# [5, 0, -3, 8, 5, -3, 10, 0, 2]
# 🎯 Твоя задача:
# Удалить все повторяющиеся значения
# Убрать отрицательные числа
# Отсортировать результат по возрастанию
# Вывести итоговый список

list_1 = [5, 0, -3, 8, 5, -3, 10, 0, 2]
list_2 = list(set(list_1))
i = 0
while i < len(list_2):
    if list_2[i] < 0:
        del list_2[i]
    else:
        i += 1

sorted_list = sorted(list_2)
print(sorted_list)

list_3 = [5, 0, -3, 8, 5, -3, 10, 0, 2]
lst = sorted([x for x in set(list_3) if x >= 0 ])
print(lst)

# Задача 1 — Нормализация строки (логин)
# Условие:
# На вход подается строка s. Нужно:
# убрать ведущие/замыкающие пробелы,
# заменить все последовательности пробелов внутри строки на один _,
# перевести результат в нижний регистр.
# Пример:
# "  Ivan   Petrov  "  →  "ivan_petrov"

login = "  Ivan   Petrov  "
login1 = login.strip()
login2 = login1.split()
login3 = "_".join(login2)
login4 = login3.lower()
print(login4)

# Задача 2 — Выделение чисел из сырого ввода
# Условие:
# Дана строка:
text = "12 cats, 7 dogs,  100  birds and two"
# Нужно:
# Найти в ней все целые числа (12, 7, 100).
# Вывести их сумму (в этом примере — 119).
current = ""
numbers =[]
for i in text:
    if i.isdigit():
        current += i
    else:
        if current != "":
            numbers.append(int(current))
            current = ""
print(numbers)
print(sum(numbers))

# Лёгкая тренировка (разогрев):
# Дан список чисел:
nums = [5, 12, 7, 20, 3, 15, 8]
# Оставь только те, что больше 10, и сохрани их в новый список.
filied = []
for num in nums:
    if num >= 10:
        filied.append(num)
print(filied)

# Задача: Подсчёт статусов
# У тебя есть список:
logs = ["OK", "FAIL", "OK", "OK", "FAIL"]
# Нужно:
# Посчитать, сколько раз встретился "OK".
# Посчитать, сколько раз встретился "FAIL".
# Вывести оба числа.

count_ok = 0
count_fail = 0

for log in logs:
    if log == "OK":
        count_ok += 1
    elif log == "FAIL":
        count_fail += 1
print(count_ok)
print(count_fail)


logs = ["OK", "FAIL", "OK", "TIMEOUT", "OK", "ERROR", "FAIL", "SKIP", "FAIL"]
dict_s = {}


for log in logs:
    if log in dict_s:
        dict_s[log] += 1
    else:
        dict_s[log] = 1

print(dict_s)


dict1 = {'OK': 3, 'FAIL': 3, 'TIMEOUT': 1, 'ERROR': 1, 'SKIP': 1}


max_value = 0

for key, value in dict1.items():
    if value > max_value:
        max_value = value
keys = []
for key, value in dict1.items():
    if value == max_value:
        keys.append(key)

print(f"Самый частый статус {keys}, {max_value} раз")


# Дан список:
items = ["a", "b", "a", "c", "b", "d", "a"]
# Нужно:
# Убрать все повторы,
# Но сохранить порядок первых вхождений.
# Ожидаемый результат:
# ["a", "b", "c", "d"]
# 🔑 Подсказки:
# Заведи пустой список unique = [].
# Заведи пустое множество seen = set() (оно быстро проверяет, встречался ли элемент раньше).
# Пройдись циклом по items:
# если элемента ещё нет в seen → добавь его и в unique, и в seen.
# если уже есть → пропусти.
# В конце выведи unique.

unique = []
seen = set()

for item in items:
    if item not in seen:
        unique.append(item)
        seen.add(item)

print(unique)


# s = str(input()).lower()
# g = 0
# sog = 0
# for i in s:
#     if i.isalpha():
#         if i in "аеёиоуыэюяaeiou":
#             g += 1
#         else:
#             sog += 1
# print(g, sog)

# Задача — сумма чётных чисел
# Дан список:
nums = [1, 4, 7, 12, 15, 18, 21]
# Нужно:
# пройтись по списку,
# найти все чётные числа (делятся на 2 без остатка),
# посчитать их сумму,
# вывести результат.

total_nums = 0

for num in nums:
    if num % 2 == 0:
        total_nums += num

print(total_nums)

# Задача — посчитать количество слов в строке
# Условие:
# Пользователь вводит строку, например:

# Программа должна вывести количество слов. В этом примере — 5.
# 🔑 Подсказки:
# слова обычно разделяются пробелами,
# у строки есть метод, который «режет» строку на список слов,
# чтобы узнать количество элементов в списке, используется функция, которую ты уже применял для строк и списков.
strings = "Я учу Python каждый день"
stirng = len(strings.split())
print(stirng)


# Задача — найти минимум и максимум
# Условие:
# Дан список:

# Нужно:
# найти минимальное и максимальное число в списке,
# при этом нельзя использовать встроенные функции min() и max().
# 🔑 Подсказки:
# Возьми первый элемент списка и запиши его и в min_val, и в max_val.
# Пройди циклом по остальным элементам:
# если число меньше min_val → обнови min_val,
# если число больше max_val → обнови max_val.
# После цикла выведи оба значения.
nums = [10, 3, 27, 5, 18, 2]
min_val = nums[0]
max_val = nums[0]
for num in nums:
    if num < min_val:
        min_val = num
    elif num > max_val:
        max_val = num
print(min_val, max_val)


# Задача — Среднее арифметическое чисел
# Дан список:
nums = [4, 7, 10, 2, 5]
# Нужно:
# посчитать сумму всех чисел,
# разделить её на количество элементов в списке,
# вывести результат (среднее значение).
# 🔑 Подсказки:
# заведи переменную total = 0 и суммируй все числа в цикле;
# количество элементов возьми через функцию, которая возвращает длину списка;
# не забудь: деление должно быть «обычным», чтобы получить число с дробной частью.

total = 0
for i in nums:
    total += i
    print(i)
result = total / len(nums)
print(total)
print(result)


# Задача — посчитать чётные и нечётные числа
# Дан список:
nums = [4, 7, 10, 2, 5, 9, 12]
# Нужно:
# посчитать, сколько в списке чётных чисел,
# и сколько нечётных,
# вывести оба результата.
# 🔑 Подсказки:
# заведи два счётчика, например even_count и odd_count,
# пройдись по списку циклом,
# если число делится на 2 без остатка → увеличивай even_count,
# иначе → увеличивай odd_count,
# в конце выведи оба значения.
even_count = 0
odd_count = 0

for i in nums:
    if i %2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f" четные числа :{even_count}")
print(f"четные числа :{odd_count}")
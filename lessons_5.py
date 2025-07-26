# адача 1 (Доступ к элементам словаря)
# Дан словарь:
# python
# user = {
#     "id": 101,
#     "name": "Алексей",
#     "is_active": True
# }
# Выведи значение ключа "name" на экран.
from copy import deepcopy

from Lessons_1 import language

user = {
    "id": 101,
    "name": "Алексей",
    "is_active": True
}
user_name = user["name"]
print(user_name)

# Задача 2
# Дан словарь:
# python
# car = {
#     "brand": "Toyota"
# }
# Добавь в него ключ "model" со значением "Camry", затем выведи обновлённый словарь.

car = {"brand": "Toyota"}

car["model"] = "Camry"
print(car)

# Следующая задача 3 (Удаление элементов из словаря):
# Дан словарь:
#
# python
# fruit = {
#     "name": "яблоко",
#     "color": "зелёное",
#     "price": 0.99
# }
# Удали ключ "price" и выведи изменённый словарь.

fruit = {
    "name": "яблоко",
    "color": "зеленое",
    "price": 0.99
}

del fruit["price"]
print(fruit)

# Следующая задача 4 (Проверка наличия ключа):
# Дан словарь:
#
# python
# device = {
#     "type": "smartphone",
#     "os": "Android",
#     "year": 2022
# }
# Проверь, есть ли в словаре ключ "os".
# Если есть — выведи "Операционная система: " + её значение, иначе — "ОС не указана".

device = {
    "type": "smartphone",
    "os": "Android",
    "year": 2022
}
 # с помощью ассерта
assert  "os" in device.keys()
# так захотел дипсик
if "os" in device:
    print("Операционная система: " + device["os"])
else:
    print("ОС не указана")

# Следующая задача 5 (Методы словарей):
# Дан словарь:
# python
# country = {
#     "name": "Япония",
#     "capital": "Токио",
#     "population": 125_800_000
# }
# Выведи список всех ключей этого словаря.

country = {
    "name": "Япония",
    "capital": "Токио",
    "population": 125_800_000
}

print(country.keys())

# Следующая задача 6 (Работа со значениями):
# Дан словарь:
# python
# movie = {
#     "title": "Крестный отец",
#     "year": 1972,
#     "director": "Ф.Ф. Коппола"
# }
# Выведи список всех значений этого словаря.

movie = {
    "title": "Крестный отец",
    "year": 1972,
    "director": "Ф.Ф. Коппола"
}

print(movie.values())

# Следующая задача 7 (Проверка наличия значения):
# Дан словарь:
#
# python
# product = {
#     "id": 543,
#     "name": "Ноутбук",
#     "in_stock": False
# }
# Проверь, есть ли в словаре значение False (именно булево), и выведи "Товар отсутствует", если это так.

product = {
    "id": 543,
    "name": "Ноутбук",
    "in_stock": False
}
if False in product.values():
    print("Товар отсутствует")
else:
    print("не так")

# Следующая задача 8 (Обновление словаря):
# Дан словарь:
# python
# profile = {
#     "name": "Мария",
#     "age": 25
# }
# Обнови словарь, добавив ключ "city" со значением "Москва" и измени возраст на 26. Выведи итоговый словарь.

profile = {
    "name": "Мария",
    "age": 25
}

profile["city"] = "Москва"
profile["age"] = 26
print(profile)

# Следующая задача 9 (Метод .get()):
# Дан словарь:
#
# python
# settings = {
#     "theme": "dark",
#     "notifications": True
# }
# Проверь значение ключа "language". Если ключа нет — выведи "Язык: по умолчанию".

settings = {
    "theme": "dark",
    "notifications": True
}

language = settings.get("Language", "Язык по умолчанию")

print(f"Язык {language}")

# Задача 10 (Метод .get())
# Дан словарь:
#
# python
# user_stats = {
#     "level": 15,
#     "health": 200
# }
# Проверь значение ключа "score". Если ключа нет — присвой переменной current_score значение 0 и выведи:
# "Текущий счёт: 0".

user_stats = {
    "level": 15,
    "health": 200
}
current_score= user_stats.get("score", 0)
print(f"Текущий счет: {current_score}")

# Задача 11 (Метод .items())
# Дан словарь:
# python
# animal = {
#     "type": "кошка",
#     "name": "Мурка",
#     "age": 2
# }
# Выведи первую пару ключ-значение из этого словаря, используя метод .items() и преобразование в список.

animal = {
    "type": "кошка",
    "name": "Мурка",
    "age": 2
}

print(list(animal.items())[0])

# адача 13 (Обновление вложенного словаря)
# Дан словарь:
#
# python
# user = {
#     "id": 101,
#     "profile": {
#         "name": "Ирина",
#         "city": "Москва"
#     }
# }
# Измени город (city) на "Санкт-Петербург".
#
# Добавь в профиль новый ключ "age" со значением 25.

user = {
    "id": 101,
    "profile": {
        "name": "Ирина",
        "city": "Москва"
    }
}
user["profile"]["city"] = "Санкт-Петербург"
user["profile"]["age"] = 25
print(user)

# Следующая задача 14 (Доступ к вложенным данным):
# Дан словарь:
#
# python
# library = {
#     "name": "Центральная библиотека",
#     "books": {
#         "fantasy": {
#             "title": "Властелин Колец",
#             "count": 5
#         }
#     }
# }
# Выведи количество экземпляров книги (count).

library = {
    "name": "Центральная библиотека",
    "books": {
        "fantasy": {
            "title": "Властелин Колец",
            "count": 5
        }
    }
}

counter = library["books"]["fantasy"]["count"]
print(counter)

# Следующая задача 15 (Комбинированная работа):
# Дан словарь:
# python
# game = {
#     "title": "The Witcher 3",
#     "platforms": ["PC", "PS4", "Xbox"],
#     "stats": {
#         "rating": 9.8,
#         "completed": True
#     }
# }
# Выведи список платформ (platforms), на которых доступна игра.
# Измени значение completed на False.
# python
game = {
    "title": "The Witcher 3",
    "platforms": ["PC", "PS4", "Xbox"],
    "stats": {
        "rating": 9.8,
        "completed": True
    }
}

game["stats"]["completed"] = False
result = game["platforms"]
print(result)

# Задача 17 (Метод .update())
# Дан словарь:
# python
# config = {
#     "version": 2.1,
#     "environment": "production"
# }
# и словарь для обновления:
# python
# update_data = {"debug": False, "max_users": 100}
# Используй метод .update(), чтобы добавить параметры из update_data в config. Выведи обновлённый словарь.

config = {
    "version": 2.1,
    "environment": "production"
}

update_data = {
    "debug": False,
    "max_users": 100
}

config.update(update_data)
print(config)

# Следующая задача 18 (Копирование словарей):
# Дан словарь:
#
# python
# original = {
#     "name": "Тест",
#     "settings": {"color": "red"}
# }
# Создай глубокую копию original (чтобы изменения в копии не затрагивали исходник). Назови копию copied_dict.
#
# (Подсказка: используй import copy и copy.deepcopy())
import copy

original = {
    "name": "Тест",
    "settings": {"color": "red"}
}

copy_dict = copy.deepcopy(original)

# Следующая задача 19 (Метод .setdefault())
# Дан словарь:
#
# python
# data = {
#     "user": "admin",
#     "level": 2
# }
# Проверь, есть ли ключ "password". Если нет — добавь его со значением "12345"
# одной операцией, используя .setdefault(). Выведи обновлённый словарь.

data = {
    "user": "admin",
    "level": 2
}

data.setdefault("password", 12345)
print(data)

# Следующая задача 20 (Комбинированная):
# Дан словарь:
#
# python
# server = {
#     "ip": "192.168.1.1",
#     "status": "active",
#     "services": ["HTTP", "SSH"]
# }
# Добавь новый сервис "DNS" в список services.
#
# Измени статус на "maintenance".
#
# Проверь, есть ли ключ "location". Если нет — добавь его со значением "unknown" (используй .get() или .setdefault()).

server = {
    "ip": "192.168.1.1",
    "status": "active",
    "services": ["HTTP", "SSH"]
}

server["services"].append("DNS")
server["status"] = "maintenance"
server.setdefault("location","unknown")
print(server)

# Следующая задача 21 (Максимально конкретная):
# Дан словарь:
#
# python
# user = {
#     "id": 101,
#     "name": "Алексей",
#     "access_levels": ["read"]
# }
# Требуется:
# Добавить строку "write" в список access_levels (использовать .append()).
# Проверить наличие ключа "email":
# Если нет — добавить его со значением None (использовать .setdefault()).
# Вывести только список access_levels после изменений.
# Напиши решение! 😊


user = {
    "id": 101,
    "name": "Алексей",
    "access_levels": ["read"]
}

user["access_levels"].append("write")
user.setdefault("email")
print(user["access_levels"])

# Следующая задача 22 (Чёткая формулировка):
# Дан словарь:
# python
# task = {
#     "title": "Документация",
#     "status": "open",
#     "tags": ["urgent"]
# }
# Требуется:
# Добавить строку "feature" в список tags (использовать .append())
# Изменить status на строку "in_progress"
# Проверить наличие ключа "assignee":
# Если нет — добавить его со значением "unassigned" (использовать .setdefault())
# Вывести только изменённый список tags
# (Ожидаемый вывод для текущих данных: ['urgent', 'feature'])
# Напиши решение! 📝


task = {
    "title": "Документация",
    "status": "open",
    "tags": ["urgent"]
}
task["tags"].append("feature")
task["status"] = "in_progress"
task.setdefault("assignee", "unassigned")
print(task["tags"])


# Финальная задача 23 (Повторение пройденного):
# Дан словарь:
# python
# project = {
#     "name": "Website Redesign",
#     "team": {
#         "design": ["Alice", "Bob"],
#         "dev": ["Charlie"]
#     }
# }
# Требуется:
# Добавить разработчика "Diana" в список dev (использовать .append())
# Проверить наличие ключа "budget":
# Если нет — добавить его со значением 10000 (использовать .setdefault())
# Вывести всю структуру team после изменений

project = {
    "name": "Website Redesign",
    "team": {
        "design": ["Alice", "Bob"],
        "dev": ["Charlie"]
    }
}
project["team"]["dev"].append("Diana")
project.setdefault("budget", 10000)
print(project["team"])


# Задача 1 (Доступ к элементам словаря по ключу)
# Дан словарь:
# python
# phone = {"brand": "Xiaomi", "model": "Redmi Note 10", "price": 25000}
# Выведите значение, связанное с ключом "model".
# Требования:
# Используйте синтаксис обращения к элементу словаря по ключу (квадратные скобки или метод get()).
# Вывод должен содержать только значение (без лишнего текста).
# Напишите ваш код, и я подскажу, если нужно что-то исправить!
# Для следующей задачи скажите «Следующая» 🔥
# P.S. Если задача кажется слишком простой/сложной — дайте знать!

phone = {
    "brand": "Xiaomi",
         "model": "Redmi Note 10",
         "price": 25000
    }

print(phone.get("model"))

# Задача 2 (Добавление и обновление элементов словаря)
# Дан словарь:
# python
# laptop = {"brand": "Lenovo", "model": "IdeaPad"}
# Добавьте ключ "year" со значением 2023.
# Обновите значение ключа "model" на "ThinkPad".
# Требования:
# Используйте квадратные скобки [] для добавления/обновления.
# Выведите изменённый словарь после всех операций.

laptop = {"brand": "Lenovo", "model": "IdeaPad"}
laptop["year"] = 2023
laptop["model"] = "ThinkPad"
print(laptop)


# Задача 3 (Удаление элементов словаря)
# Дан словарь:
# python
# student = {"name": "Анна", "age": 21, "group": "B-205", "gpa": 4.8}
# Удалите ключ "gpa" тремя разными способами и после каждого удаления выводите изменённый словарь.
# Способы:
# Через del
# Через метод .pop()
# Через создание нового словаря без ключа (генератор словаря или {k:v for})
# Требования:
# Каждый способ должен быть реализован отдельно (не в одном цикле).
# После каждого удаления выводите словарь.

student = {"name": "Анна", "age": 21, "group": "B-205", "gpa": 4.8}

student.pop("gpa")
print(student)

student = {"name": "Анна", "age": 21, "group": "B-205", "gpa": 4.8}

del student["gpa"]
print(student)

# Задача 4 (Проверка наличия ключа/значения)
# Дан словарь:
# python
# inventory = {"item": "ноутбук", "quantity": 15, "price": 87000, "warehouse": "Москва"}
# Проверьте, есть ли в словаре ключ "price".
# Проверьте, есть ли среди значений число 15.
# Для каждой проверки выведите True или False (без if).
# Требования:
# Используйте методы словаря:
# Для ключей: .get() или оператор in.
# Для значений: метод .values() + in.
# Вывод должен быть в формате:
# text
# Ключ 'price' есть: True
# Значение 15 есть: True

inventory = {"item": "ноутбук", "quantity": 15, "price": 87000, "warehouse": "Москва"}
print("Ключ  price есть:", "price" in inventory)
print("Значение 15 есть:", 15 in inventory.values())


# Задача 5 (Получение элементов, ключей и значений словаря)
# Дан словарь:
# python
# movie = {
#     "title": "Интерстеллар",
#     "year": 2014,
#     "director": "Кристофер Нолан",
#     "genre": "фантастика"
# }
# Выведите все ключи словаря в виде списка.
# Выведите все значения словаря в виде списка.
# Выведите все пары ключ-значение в виде списка кортежей.
# Требования:
# Используйте методы словаря: .keys(), .values(), .items().
# Результат каждого пункта выводите отдельно с пояснением:

movie = {
    "title": "Интерстеллар",
    "year": 2014,
    "director": "Кристофер Нолан",
    "genre": "фантастика"
}

print("Ключи:", list(movie.keys()))
print("Значения:", list(movie.values()))
print("Пары:", list(movie.items()))


# Финальная задача: Работа со словарём (упрощённая версия)
# Цель: Закрепить базовые операции со словарями.
#
# Дан словарь:
# python
# Задание:
# Проверка наличия ключа
# Проверьте, есть ли в словаре ключ "storage". Выведите True или False.
# Добавление нового ключа
# Добавьте ключ "os" со значением "iOS 15".
# Удаление ключа
# Удалите ключ "year".
# Вывод списка цветов
# Выведите каждый цвет из списка "colors" отдельной строкой (без join()).
# Вывод итогового словаря
# Покажите, как выглядит словарь после всех изменений.


smartphone = {
    "brand": "Apple",
    "model": "iPhone 13",
    "price": 79900,
    "year": 2021,
    "colors": ["чёрный", "белый", "синий"]
}

print("Есть ли в словаре ключ 'storage':", "storage" in smartphone)
smartphone["os"] = "IOS 15"
del smartphone["year"]
print("Доступные цвета:")
for color in smartphone["colors"]:
    print(color)
print("Итоговый словарь:", smartphone)


# Задача: "Фруктовая корзина"
# Дан словарь с фруктами и их количеством:
# python
# basket = {
#     "Яблоко": 5,
#     "Банан": 3,
#     "Апельсин": 2,
#     "Груша": 0  # Закончились
# }
# Задание:
# Выведите только те фрукты, количество которых больше 0, в формате:
# text
# Яблоко - 5 шт.
# Банан - 3 шт.
# Апельсин - 2 шт.
# Для фруктов с количеством 0 выведите:
# text
# Груша - закончилась


basket = {
    "Яблоко": 5,
    "Банан": 3,
    "Апельсин": 2,
    "Груша": 0
}
for fruit, title in basket.items():
    if title > 0:
        print(f"{fruit} {title}")
    else:
        print(f"{fruit} - закончилась!")


# Задача 1: Доступ к элементам
# Дан словарь:
# python
# book = {
#     "title": "Гарри Поттер",
#     "author": "Дж. Роулинг",
#     "year": 1997
# }
# Задание: Выведите значение ключа "author".
# Подсказка: Используйте квадратные скобки [] или метод .get().

book = {
    "title": "Гарри Поттер",
    "author": "Дж. Роулинг",
    "year": 1997
}
print(book.get("author"))
print(book["author"])

# адача 2: Добавление элемента
# Дан словарь:
#
# python
# car = {
#     "brand": "Toyota",
#     "model": "Camry"
# }
# Задание: Добавьте ключ "year" со значением 2020.

car = {
    "brand": "Toyota",
    "model": "Camry"
}
car["year"] = 2020
print(car)


# Задача 3: Удаление элемента
# Дан словарь:
#
# python
# student = {
#     "name": "Алексей",
#     "age": 20,
#     "group": "A-101"
# }
# Задание: Удалите ключ "age" двумя способами:

# student = {
#     "name": "Алексей",
#     "age": 20,
#     "group": "A-101"
# }
# student.pop("age")
# print(student)
#
# del  student["age"]
# print(student)


# Задача 4: Проверка ключей
# Дан словарь:
#
# python
# weather = {
#     "city": "Москва",
#     "temp": 25,
#     "humidity": 80
# }
# Задание: Проверьте, есть ли ключ "temp" в словаре, и выведите True или False.

weather = {
    "city": "Москва",
    "temp": 25,
    "humidity": 80
}

print("есть ли ключ 'temp' в словаре", "temp" in weather)

# Задача 5: Обход словаря
# Дан словарь:
# python
# fruits = {
#     "apple": "red",
#     "banana": "yellow",
#     "orange": "orange"
# }
# Задание: Выведите все пары ключ: значение в формате:\
# apple - red
# banana - yellow
# orange - orange
# text


fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange"
}

for fruit, color in fruits.items():
    print(f"{fruit} - {color}")

# Уровень 2: Практические задачи
# Задача 6: Обновление значений
#
# python
# inventory = {
#     "apples": 50,
#     "oranges": 30,
#     "bananas": 45
# }
# Уменьшите количество апельсинов на 10
#
# Добавьте новые товары: "pears" (40) и "peaches" (25)

inventory = {
    "apples": 50,
    "oranges": 30,
    "bananas": 45
}

inventory["oranges"] = 20
inventory["pears"] = 40
inventory["peaches"] = 25
print(inventory)

# Задача 7: Поиск по значению
#
# python
# employees = {
#     "Alice": "developer",
#     "Bob": "manager",
#     "Charlie": "developer"
# }
# Найдите всех разработчиков (выведите их имена)

employees = {
    "Alice": "developer",
    "Bob": "manager",
    "Charlie": "developer"
}

developers = employees.get("developer")
print(developers)


# Задача 8: Слияние словарей
#
# python
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# Объедините их в один словарь

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)


# Задача 9: Глубокое обновление словаря
# Дан словарь с вложенной структурой:
#
# python
# shop = {
#     "fruits": {
#         "apples": 50,
#         "oranges": 30
#     },
#     "vegetables": {
#         "carrots": 20,
#         "potatoes": 40
#     }
# }
# Задание:
#
# Уменьшите количество "oranges" на 10.
#
# Добавьте новый овощ "tomatoes" со значением 35.
#
# Выведите обновлённый словарь.

shop = {
    "fruits": {
        "apples": 50,
        "oranges": 30
    },
    "vegetables": {
        "carrots": 20,
        "potatoes": 40
    }
}

shop["fruits"]["oranges"] -= 10
shop["vegetables"]["tomatoes"] = 35
print(shop)


# Задача 10: Фильтрация словаря
# Дан словарь товаров:
#
# python
# products = {
#     "laptop": 1200,
#     "mouse": 30,
#     "keyboard": 80,
#     "monitor": 250
# }
# Задание:
#
# Создайте новый словарь, где останутся только товары дешевле 100.
#
# Выведите результат в формате:
#
# text
# Дешёвые товары:
# mouse - 30
# keyboard - 80
# Подсказка: Используйте генератор словаря:
#
# python
# {key: value for key, value in products.items() if value < 100}
products = {
    "laptop": 1200,
    "mouse": 30,
    "keyboard": 80,
    "monitor": 250
}
print("Дешевые товары:")
for key, value in products.items():
    if value < 100:

        print(f"{key} - {value}")

# Уровень 3: Продвинутые задачи
# Задача 12: Словарь из двух списков
# Даны:
# python
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# Создайте из них словарь {"name": "Alice", "age": 25, "city": "New York"}.

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

print(dict(zip(keys,values)))

# адача 13: Поиск максимального значения
# Дан словарь:
#
# python
# grades = {"Math": 90, "Science": 85, "History": 78}
# Найдите предмет с наивысшим баллом и выведите:
# "Лучший результат: Math (90)".

grades = {"Math": 90, "Science": 85, "History": 78}
best_subject = max(grades, key=grades.get)
print(f"Лучший результат: {best_subject} ({grades[best_subject]})")
import copy

original = {
    "a": 1,
    "b": {"x": 10, "y": 20}
}
dict1 = copy.deepcopy(original)
print(dict1)


# Задача 15: Обратный словарь
# Дан словарь переводов:
# python
# translations = {
#     "apple": "яблоко",
#     "banana": "банан",
#     "orange": "апельсин"
# }
# Задание:
# Создайте новый словарь, где ключи и значения поменяются местами:
# python
# {
#     "яблоко": "apple",
#     "банан": "banana",
#     "апельсин": "orange"
# }


translations = {
    "apple": "яблоко",
    "banana": "банан",
    "orange": "апельсин"
}

reversed_dict = {value: key  for key, value in translations.items()}
print(reversed_dict)
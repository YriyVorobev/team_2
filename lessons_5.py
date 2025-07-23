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

car = {
    "brand": "Toyota"
}

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
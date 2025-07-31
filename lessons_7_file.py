# Задача 1 (Работа с файлами)
# Создай файл notes.txt и запиши в него строку: "Моя первая запись".
# Подсказка: Используй режим записи ('w').
# Что проверяем:
# Правильное открытие файла.
# Корректное закрытие файла (можно через with).
from os import write

from lessons_5 import config, country
from lessons_6 import count

# with open("file_name.txt", "w+") as file:
#     file.write("Моя первая запись")
#     file.seek(0)
#     read = file.read()
#     print(read)


# Задача 2 (Чтение файлов)
# Есть файл data.txt с содержимым:
# text
# Первая строка
# Вторая строка
# Третья строка
# Напишите код, который выводит только вторую строку из этого файла.

# with open("file_name.txt", "r") as file:
#     reads = file.readlines()
#     print(reads[1])


# Задача 3 (Добавление в файл)
# Дан файл notes.txt с содержимым:
# text
# Первая запись
# Допиши в этот файл строку "Вторая запись" без перезаписи существующего содержимого.
# Подсказка: Используй режим дополнения (не "w").
# Проверь:
# После выполнения файл должен содержать:
# text
# Первая запись
# Вторая запись
# Жду решение! 😊

# with open("file_name.txt", "a") as file:
#     file.write("\nВторая строка")

# Задача 1.
# Создай текстовый файл с названием numbers.txt и запиши в него числа от 1 до 5, каждое с новой строки.

# file = open("file_name.txt","w",encoding = "UTF-8")
# file.write("1\n2\n3\n4\n5")
# file.close()

# Задача 2.
# Открой файл file_name.txt из предыдущей задачи, прочитай его содержимое и выведи построчно в консоль.

# file = open("file_name.txt", "r")
# content = file.read()
# print(content)
# file.close()
#
#
# Задача 3. Добавление данных в файл
# Открой файл file_name.txt в режиме добавления и запиши в него числа от 6 до 10, каждое с новой строки.
# Условия:
# Используй режим "a" (append)
# Не забудь закрыть файл
# Проверь результат — после запуска файл должен содержать числа от 1 до 10

# file = open("file_name.txt", "a")
# file.write("\n6\n7\n8\n9\n10")
# file.close()


# with open("file_name.txt", "r") as file:
#     lines = file.readlines()
#     total = 0
# for line in lines:
#     num = int(line.strip())
#     total += num
# print(total)


# Задача.
# Создай файл hello.txt и запиши в него одну строку: "Привет, мир!".
# Условия:
# Используй контекстный менеджер with
# Файл должен быть создан в той же папке, где находится скрипт
# Режим записи — "w"
# Что проверить после выполнения:
# Открой файл hello.txt вручную и убедись, что там есть строка "Привет, мир!"
# Напиши свой код, и я подскажу, если нужно что-то исправить!


with open("hello.txt", "w") as file:
    file.write("Привет мир!")


# Задача 2 (чтение файла).
# Прочитай файл hello.txt и выведи его содержимое в консоль.
# Условия:
# Используй with
# Режим — "r"
# Вывод должен быть без лишних пустых строк
# Напиши решение!

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Задача 3 (добавление в файл).
# Добавь в файл hello.txt вторую строку: "Это мой первый файл!".
# Условия:
# Используй режим "a" (append)
# Не удаляй существующее содержимое
# Новая строка должна быть с новой строки (используй \n)
# Напиши решение!
with open("hello.txt", "a") as file:
    file.write("\nЭто мой первый файл!")

# Задача 4 (подсчёт строк).
# Напиши код, который подсчитает и выведет количество строк в файле hello.txt.
# Условия:
# Используй with
# Примени метод readlines()
# Вывод в формате: "Количество строк: N"

with open("hello.txt", "r") as file:
    lines = len(file.readlines())
    print(f"Количество строк: {lines}")

# Задача 5.
# Создай новый файл numbers.txt и запиши в него числа от 1 до 5, каждое с новой строки.
# Условия:
# Используй with
# Режим записи - "w"
# Каждое число должно быть на отдельной строке


# with open("numbers.txt", "w") as file:
#     file.write("1\n2\n3\n4\n5")

with open("numbers.txt", "w") as file:
    for numbers in range(1, 6):
        file.write(f"{numbers}\n")

# Задача.
# Создай файл products.txt и запиши в него 3 продукта (каждый с новой строки):
# text
# Хлеб
# Молоко
# Яблоки
# Затем добавь четвертый продукт: "Сахар"
# Прочитай файл и выведи все продукты в формате:
# text
# 1. Хлеб
# 2. Молоко
# 3. Яблоки
# 4. Сахар

# with open("products.txt", "w") as file:
#     file.write("Хлеб\nМолоко\nЯблоки")
# with open("products.txt", "a") as file:
#     file.write("\nСахар")
# with open("products.txt", "r") as file:
#     for index, line in enumerate(file, 1):
#         print(f"{index}. {line.strip()}")

# Отлично! Вот Задача 8 (работа с текстом в файлах):
# Задача.
# Создай файл fruits.txt и запиши в него:
# text
# Яблоко
# Груша
# Яблоко
# Апельсин
# Яблоко
# Затем подсчитай, сколько раз слово "Яблоко" встречается в файле, и выведи результат:
# "Слово 'Яблоко' встречается 3 раза".
# Условия:
# Используй with для всех операций.
# Для подсчёта примени метод .count().
# Регистр имеет значение ("Яблоко" ≠ "яблоко").


# with open("fruits.txt", "w") as file:
#     file.write("Яблоко\nГруша\nЯблоко\nАпельсин\nЯблоко")
#
# with open("fruits.txt", "r") as file:
#     content = file.read()
#     count = content.count("Яблоко")
#     print(f"Слово 'Яблоко' встречается {count} раз")

# адача 10 (базовая)
# Создай файл city.txt и запиши в него название своего города.
# Затем прочитай файл и выведи:
# "Я живу в городе [название]".

# with open("city.txt", "w") as file:
#     file.write("Краснодар")
#
# with open("city.txt", "r") as file:
#     city = file.read()
#     print(f"Я живу в городе {city}")

# Отлично! Вот Задача 11 (простое добавление в файл):
# Задача.
# Возьми файл city.txt из прошлой задачи (где записан «Краснодар»).
# Добавь второй город на новой строке (например, «Москва»).
# Прочитай файл и выведи все города через запятую в одной строке:
# "Города: Краснодар, Москва".

with open("city.txt", "a") as file:
    file.write("\nМосква")

with open("city.txt", "r") as file:
    content = file.readlines()
    cities = [line.strip() for line in content]
    print(f"Города:{', '.join(cities)}")

# Задача 12
# Создай файл game.txt и запиши в него название своей любимой игры
# Прочитай файл и выведи сообщение:
# "Моя любимая игра: [название из файла]"

with open("game.txt", "w+") as file:
    file.write("Game of Thrones")
    file.seek(0)
    content = file.read()
    print(f"Моя любимая игра: {content}")

# Отлично! Вот Задача 13 (работа с несколькими файлами):
# Задача.
# Создай два файла:
# animals.txt (запиши туда: "Кот")
# birds.txt (запиши туда: "Сова")
# Прочитай оба файла и выведи сообщение:
# "Любимые питомцы: [животное] и [птица]"

with open("animals.txt", "w") as file:
    file.write("Кот")
with open("birds.txt", "w") as file:
    file.write("Сова")
with open("animals.txt","r") as file:
    animal = file.read().strip()
with open("birds.txt", "r") as file:
    bird = file.read().strip()
    print(f"Любимые питомцы: {animal} и {bird}")

    # Отлично! Вот Задача 14 (простая работа с числами):
    # Задача.
    # Создай файл prices.txt и запиши в него 3 цены через запятую:
    # text
    # 100,150,200
    # Прочитай файл, подсчитай сумму чисел и выведи:
    # "Общая сумма: [сумма] руб."
    # Условия:
    # Используй with
    # Раздели числа методом .split(",")
    # Преобразуй строки в числа (int)

with open("prices.txt", "w") as file:
    file.write("100, 150, 200")
with open("prices.txt", "r") as file:
    read = file.read().split(", ")
    summ = sum(int(x) for x in read)
    print(f"Общая сумма: {summ}")

# Задача 15
# Создай файл grades.txt и запиши в него 5 оценок через запятую (например: 3,5,4,5,4).
# Прочитай файл и вычисли:
# Средний балл (сумма всех оценок / их количество)
# Сколько раз встречается оценка 5

with open("grades.txt", "w") as file:
    file.write("3, 4, 4, 5, 4")

with open("grades.txt", "r") as file:
    content = file.read().split(", ")
    grades = [int(x) for x in content]
    avg = sum(grades) / len(grades)
    fives = grades.count(5)
    print(f"Средний балл: {avg:.2f}")
    print(f"Пятерок: {fives}")

# тлично! Вот Задача 16 (максимально простая, но полезная):
# Задача.
# Создай файл colors.txt и запиши в него 3 любимых цвета, каждый с новой строки. Например:
# text
# Красный
# Синий
# Зелёный
# Прочитай файл и выведи цвета в обратном порядке (сначала последний, потом первый).
# Условия:
# Используй with
# Режимы: "w" для записи, "r" для чтения
# Для обращения порядка: reversed() или [::-1]

with open("colors.txt", "w") as file:
    file.write("Красный, Синий, Зелёный")

with open("colors.txt", "r") as file:
    colors = file.read().split(", ")
    for color in reversed(colors):
        print(f"Цвет {color}")






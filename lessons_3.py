# Отлично! Начинаем с первой задачи.
# Задача 1 (Получение элементов списка):
# Дан список numbers = [10, 20, 30, 40, 50]. Выведи второй элемент списка.
# Напиши решение, и я проверю его или дам подсказку, если нужно. 😊
from subprocess import list2cmdline

numbers = [10, 20, 30, 40, 50]
print(numbers[1])

# Задача 2:
# Дан список colors = ['red', 'green', 'blue'].
# Добавь в него цвет 'yellow'.
# Замени 'green' на 'black'.

colors = ['red', 'green', 'blue']
colors.append('yellow')
colors[1] = "black"
print(colors)


# Задача 3:
# Дан список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]. Выведи элементы с третьего по шестой

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2 : 6])

# Задача 4:
# Дан список items = ['book', 'pen', 'pencil', 'eraser'].
# Удали 'pencil' из списка.
# Очисти весь список.

items = ["book", "pen", "pencil", "eraser"]
del items[2]
print(items)
items.clear()
print(items)

# Задача 5:
# Даны два списка:
# python
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Объедини их в один список merged_list (двумя разными способами).

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)

# Задача 6:
# Дан список:
# python
# animals = ['cat', 'dog', 'fish']
# Вставь слово 'bird' между 'cat' и 'dog'.

animals = ["cat", "dog", "fish"]
animals.insert(1,"bird")
print(animals)

# Задача 7:
# Создай список fruits, содержащий три любимых фрукта.
# Напиши решение, и я проверю его!

fruits = ["яблоко", "банан", "слива"]

# Задача 8:
# Дан список:
# python
# letters = ['a', 'b', 'c', 'd']
# Замени третий элемент на 'x'.

letters = ['a', 'b', 'c', 'd']
letters[2] = 'x'
print(letters)

# Задача 9
# Дан список:
# python
# shopping = ['хлеб', 'молоко']
# Добавь 'яйца' в конец списка.
# Вставь 'сыр' на вторую позицию (между 'хлеб' и 'молоко')

shopping = ["хлеб", "молоко"]
shopping.append("яйца")
shopping.insert(1,"сыр")
print(shopping)

# git
# Задача 10
# Даны два списка:
# python
# list_a = [1, 2, 3]
# list_b = [4, 5]
# Объедини их ,чтобы list_a стал [1, 2, 3, 4, 5].

list_a = [1, 2, 3]
list_b = [4, 5]
list_a.extend(list_b)
print(list_a)

# Задача 11
# Дан список:
# python
# numbers = [10, 20, 30, 40, 50, 60]
# Удали число 30 (можно по индексу или значению).
# Выведи срез от второго до пятого элемента включительно.

numbers = [10, 20, 30, 40, 50, 60]
numbers.remove(30)
print(numbers[1:5])

# тлично! Вот первая задача из темы «Списки» для закрепления синтаксиса:
# Задача 1 (Создание списка)
# Создай список fruits, содержащий три элемента: "яблоко", "банан", "апельсин".

fruits = ["яблоко", "банан", "апельсин"]

# Отлично! Список fruits создан верно. ✅
# Задача 2 (Получение элементов списка)
# Дан список:
# python
# colors = ["красный", "зеленый", "синий", "желтый", "черный"]
# Выведи третий элемент списка

colors = ["красный", "зеленый", "синий", "желтый", "черный"]
print(colors[2])

# Задача 3 (Добавление элементов в список)
# Дан пустой список:
# python
# numbers = []
# Добавь в него числа 1, 2 и 3 (по одному за операцию), затем выведи список.

numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

# Задача 4 (Добавление в конкретное место)
# Дан список:
# python
# letters = ["a", "b", "d"]
# Вставь букву "c" между "b" и "d" (используя индекс).
# Подсказка: Нужен метод, который умеет вставлять элемент на заданную позицию.

letters = ["a", "b", "d"]

letters.insert(2,"c")
print(letters)

# Задача 5 (Удаление элементов)
# Дан список:
# python
# items = ["книга", "ручка", "ластик", "карандаш"]
# Удали "ластик" из списка двумя разными способами:
# По значению (методом),
# По индексу (командой).

items = ["книга", "ручка", "ластик", "карандаш"]

items.pop(2)
print(items)
items = ["книга", "ручка", "ластик", "карандаш"]
del items[2]

print(items)


# Задача 6 (Срезы списка)
# Дан список:
# python
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Создай новый список, содержащий только элементы с индексами от 3 до 7 (включительно), и выведи его.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:8])


# Задача 7 (Слияние списков)
# Даны два списка:
# python
# list1 = [1, 2, 3]
# list2 = ["a", "b", "c"]
# Создай один новый список, содержащий все элементы из list1 и list2 (в том же порядке), и выведи его.

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

# list3 = list1 + list2
# print(list3)
list1.extend(list2)
print(list1)


# Задача 8 (Замена элементов)
# Дан список:
# python
# words = ["яблоко", "груша", "апельсин", "виноград"]
# Замени "груша" на "банан" (используя индекс), затем выведи список.
# Подсказка: Обратись к элементу по индексу и присвой новое значение.

words = ["яблоко", "груша", "апельсин", "виноград"]
words[1] = "банан"
print(words)

# Задача 9 (Очистка списка)
# Дан список:
# python
# data = [10, 20, 30, 40, 50]
# Сделай его пустым двумя разными способами:
# Методом очистки,
# Через присваивание.
# Выведи список после каждого способа.
# Подсказка:
# Для первого способа используй метод, который удаляет все элементы.
# Для второго — присвой переменной data новое значение.

data = [10, 20, 30, 40, 50]

# data = []
# print(data)

data.clear()
print(data)

# Задача 10 (Дублирование списка)
# Дан список:
# python
# original = ["A", "B", "C"]
# Создай копию этого списка (новый список с теми же элементами)
# и назови её copied. Затем добавь в copied строку "D", но так,
# чтобы original остался без изменений.


original = ["A", "B", "C"]
copied = original.copy()
copied.append("D")
copied = list(original)
copied.append("E")
print(original)
print(copied)
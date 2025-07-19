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
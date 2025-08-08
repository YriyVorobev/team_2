# Отлично! Вот первая задача на закрепление ООП:
# Задача 1 (Создание класса)
# Создай класс Robot с тремя атрибутами уровня класса (без __init__):
# name (строка, значение по умолчанию: "R2-D2")
# power (число, значение по умолчанию: 100)
# is_activated (булево значение, по умолчанию: False)
# Проверка:
# После создания класса должно работать:


class Robot:
    name = "R2-D2"
    power = 100
    is_activated = False


print(Robot.name,Robot.power,Robot.is_activated)


# Задача 2 (Конструктор init)
# Создай класс Car с конструктором, который принимает:
# model (строка)
# year (число)
# is_working (булево значение, по умолчанию True)

class Car:
    def __init__(self,model,year,is_working=True):
        self.model = model
        self.year = year
        self.is_working = is_working


my_car = Car("Toyota",2020)
print(my_car.model)


# Задача 3 (Методы класса и self)
# Создай класс Person с:
# Конструктором, принимающим name (строка)
# Методом greet(), который возвращает строку:
# "Привет, я [name]!"
# Проверка:
# python
# p = Person("Анна")
# print(p.greet())  # Должно вывести "Привет, я Анна!"
# Подсказки (если нужны):
# Не забудь про self в методах
# Для доступа к атрибуту используй self.name
# Метод должен возвращать строку (не выводить)

class Person:
    """Имя человека"""
    def __init__(self,name):
        self.name = name

    def greet(self):
        """Приветствие человека по имени"""
        return f"Привет, я {self.name}!"


p = Person("Анна")
print(p.greet())


# Задача 4 (Комбинированная: атрибуты + методы)
# Создай класс BankAccount с:
# Атрибутами при инициализации:
# owner (владелец, строка)
# balance (баланс, число, по умолчанию 0)
# Методом deposit(amount), который увеличивает баланс на указанную сумму
# Методом show_balance(), который возвращает строку:
# "У [owner] на счету [balance] рублей"

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def show_balance(self):
        return f"У {self.owner} на счету {self.balance} рублей"

account = BankAccount("Иван")
account.deposit(500)
print(account.show_balance())


# Задача 5 (Базовый уровень ООП)
# Создай класс Book:
# С атрибутами в __init__:
# title (название, строка)
# author (автор, строка)
# is_available (доступность книги, булево значение, по умолчанию True)
# С методом borrow(), который:
# Меняет is_available на False, если книга доступна
# Возвращает строку "Книга [title] выдана"
# Если книга уже выдана, возвращает "Книга [title] недоступна"

class Book:
    def __init__(self,title,author,is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"Книга {self.title} выдана"
        else:
            return f"Книга {self.title} недоступна"


book = Book("Война и мир","Толстой Л.Н.",is_available=False)
book1 = Book("Война и мир","Толстой Л.Н.")

print(book1.borrow())
title = (book.borrow())
print(title)


# Задача 6 (Работа с атрибутами и методами)
# Создай класс CoffeeMachine:
# С атрибутами в __init__:
# water_level (уровень воды, число, по умолчанию 0)
# С методами:
# add_water(amount) — увеличивает water_level на указанное количество
# make_coffee() — если воды >= 100, уменьшает уровень на 100 и возвращает "Кофе готов", иначе "Недостаточно воды"

class CoffeMachine:

    def __init__(self):
        self.water_level = 0


    def add_water(self,amount):
        self.water_level += amount


    def make_coffe(self):
        if self.water_level >= 100:
            self.water_level -= 100
            return f"Кофе готов"
        else:
            return f"Недостаточно воды"


coffe = CoffeMachine()
coffe.add_water(150)
print(coffe.make_coffe())
print(coffe.make_coffe())


# Задача 7 (Работа со списками в классе)
# Создай класс Playlist:
# С атрибутами в __init__:
# songs (список строк-названий песен, по умолчанию пустой [])
# current_track (индекс текущей песни, по умолчанию 0)
# С методами:
# add_song(title) — добавляет песню в конец списка
# next() — переключает на следующую песню (увеличивает индекс)
# Если текущая песня последняя, возвращает "Плейлист окончен"
# play() — возвращает строку "Играет: [название текущей песни]"

class PlayList:

    def __init__(self,songs=None,current_track=0):
        self.songs = songs if songs is not None else []
        self.current_track = current_track


    def add_song(self,title):
        self.songs.append(title)
        return f"Играет трек: {title}"


    def next(self):
        self.current_track += 1
        if self.current_track >= len(self.songs):
            return f"Плейлист окончен"
        else:
            return self.play()

    def play(self):
        if not self.songs:
            return f"Список пуст"
        return f"Играет: {self.songs[self.current_track]}"

play = PlayList()
print(play.add_song(["Шафран","Музыка"]))
print(play.play())
print(play.next())
print(play.next())




# адача 8 (Класс с вычисляемым свойством)
# Создай класс Rectangle:
# С атрибутами в __init__:
# width (ширина, число)
# height (высота, число)
# С методом area(), который возвращает площадь прямоугольника (width * height)
# С методом perimeter(), который возвращает периметр (2 * (width + height))

class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangles = Rectangle(2,3)
print(rectangles.area())
print(rectangles.perimeter())

# адача 9 (Работа с несколькими объектами)
# Создай класс Student:
# С атрибутами в __init__:
# name (строка)
# grades (список оценок, по умолчанию пустой [])
# С методами:
# add_grade(grade) — добавляет оценку (число от 1 до 5) в grades
# get_average() — возвращает средний балл (или 0, если оценок нет)
# is_excellent() — возвращает True, если средний балл >= 4.5
# Подсказки (если нужны):
# Для среднего балла: sum(self.grades) / len(self.grades)
# В is_excellent() используй вызов self.get_average()
# Проверяй деление на 0 в get_average()


class Student:

    def __init__(self,name,grades=None):
        self.name = name
        self.grades = [] if grades is None else grades

    def add_grade(self,grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.get_average() >= 4.5


student = Student("Юрий")
student.add_grade(5)
print(student.name)
print(student.get_average())
print(student.is_excellent())


# Задача 6 — Объект класса
# Создай класс Lamp.
# В конструкторе задай атрибут is_on (булево), по умолчанию False.
# Добавь методы: turn_on(), turn_off(), status() — возвращает строку "Включена" или "Выключена" в зависимости от состояния.
# Создай два объекта лампы: у первой включи свет, у второй оставь выключенной.
# Убедись, что состояние у объектов независимое (каждая лампа хранит своё).

class Lamp:

    def __init__(self, is_on=False):
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        if self.is_on:
            return "Включена"
        else:
            return "Выключена"


lamp = Lamp()
lamp.turn_on()
lamp.turn_on()
print(lamp.status())
lamp.turn_off()
lamp.turn_off()
print(lamp.status())




# Задача 1 — Общие атрибуты (class attributes)
# Создай класс Lamp без __init__.
# Добавь атрибуты уровня класса: is_on = False, voltage = 220, model = "Basic".
# Ничего не выводи из класса.
# Проверка:
# После объявления класса должно работать: доступ к Lamp.is_on, Lamp.voltage, Lamp.model.
# Готово — напишите: Подсказка, Проверить (с вашим кодом) или Дальше.

class Lamp:

    is_on = False
    voltage = 220
    model = "Basic"

print(Lamp.is_on)
print(Lamp.voltage)
print(Lamp.model)


# Задача 2 — Конструктор init и self
# Создай класс User.
# В __init__(self, name, age=18) сохрани значения в атрибутах self.name и self.age.
# Ничего не выводи из класса.
# Проверка:
# После создания объекта u = User("Анна") должны быть доступны: u.name == "Анна", u.age == 18.
# Напишите: Подсказка, Проверить (с вашим кодом) или Дальше.

class User:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age


user = User("Анна")
print(user.name)
print(user.age)

# Задача 3 — Методы класса и self
# Создай класс Counter.
# В __init__(self, start=0) сохрани self.value = start.
# Метод increment(self) должен увеличивать self.value на 1 и возвращать текущее значение.
# Метод reset(self) должен обнулять self.value (делать 0).
# Проверка:
# c = Counter() → c.increment() == 1, потом c.increment() == 2
# c.reset() → c.value == 0
# Напишите: Подсказка, Проверить (с вашим кодом) или Дальше.

class Counter:

    def __init__(self,start=0):
        self.value = start


    def increment(self):
        self.value +=1
        return self.value


    def reset(self):
        self.value = 0

counter = Counter()

print(counter.increment())
print(counter.increment())
print(counter.value)
counter.reset()
print(counter.value)

# Задача 4 — Объект класса и понимание self
# Создай класс Calculator.
# В __init__(self, name="Калькулятор") сохрани self.name = name.
# Метод add(self, a, b) должен возвращать сумму a + b.
# Метод multiply(self, a, b) должен возвращать произведение a * b.
# Метод get_name(self) должен возвращать строку "Это [name]".
# Проверка:
# calc = Calculator("Мой калькулятор") → calc.get_name() == "Это Мой калькулятор"
# calc.add(5, 3) == 8, calc.multiply(4, 2) == 8
# Напишите: Подсказка, Проверить (с вашим кодом) или Дальше.

class Calculator:

    def __init__(self,name="Калькулятор"):
        self.name = name

    def add(self,a,b):
        return a + b

    def multiply(self,a,b):
        return a * b

    def get_name(self): 
        return self.name

calc = Calculator("Мой калькулятор")
print(calc.get_name())
print(calc.add(5,3))
print(calc.multiply(4,2))


# Задача 6 — Объект класса
# Создай класс Lamp.
# В конструкторе задай атрибут is_on (булево), по умолчанию False.
# Добавь методы: turn_on(), turn_off(), status() — возвращает строку "Включена" или "Выключена" в зависимости от состояния.
# Создай два объекта лампы: у первой включи свет, у второй оставь выключенной.
# Убедись, что состояние у объектов независимое (каждая лампа хранит своё).

class Lamp:

    def __init__(self, is_on=False):
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        if self.is_on:
            return "Включена"
        else:
            return "Выключена"


lamp = Lamp()
lamp.turn_on()
lamp.turn_on()
print(lamp.status())
lamp.turn_off()
lamp.turn_off()
print(lamp.status())


# Задача 7 — Общие атрибуты
# Создай класс Counter.
# Добавь общий атрибут класса total, начальное значение 0.
# В конструкторе каждый раз при создании объекта увеличивай total на 1.
# Добавь метод get_total(), который возвращает текущее значение общего счётчика.
# Проверь логику: создай три объекта и убедись, что total стал равен 3.
# Важно: total должен быть атрибутом класса, а не self.total.


class Counter:
    total = 0

    def __init__(self):
        Counter.total +=1

    def get_total(self):
        return Counter.total



counter = Counter()
counter1 = Counter()
counter2 = Counter()
print(counter.get_total())


# Задача 8 — Конструктор класса init
# Создай класс Profile.
# В __init__(self, name, city="Unknown") сохрани значения в атрибутах экземпляра.
# Добавь метод get_info(), который возвращает строку: "Name: [name], City: [city]".
# Проверь: создай два объекта — один с указанием city, другой без — и сравни результаты get_info().
# Напиши “проверь” с фрагментом твоего решения или “дай подсказку”, если застрял. Или “следующая задача”, когда будешь готов.
# Выдал задачу №8 по теме конструктора __init__

class Profile:

    def __init__(self,name,city="Unknown"):
        self.name = name
        self.city = city

    def get_info(self):
        return f"Name: {self.name}, City: {self.city}"


profile = Profile("Юрий","Краснодар")
print(profile.get_info())
profile1 = Profile("Юрий")
print(profile1.get_info())

# Задача 9 — Методы класса (экземпляра)
# Создай класс TextLine.
# В __init__(self, text="") сохрани текст в атрибуте экземпляра.
# Добавь методы:
# append(part) — добавляет к текущему тексту пробел и часть part.
# uppercase() — возвращает текущий текст в верхнем регистре (не изменяя исходный).
# clear() — очищает текст (делает пустой строкой).
# get_text() — возвращает текущий текст.
# Проверь: создай объект, добавь две части текста, выведи uppercase(), затем очисти и проверь, что get_text() пустой.
# Напиши “проверь” с фрагментом твоего решения или “дай подсказку”, если застрял. Готов будешь — скажи “следующая задача”.
# Выдал задачу №9 по теме методов экземпляра без кода
# Готов проверять или дать подсказку/следующую

class TestLine:

    def __init__(self,text=""):
        self.text = text


    def append(self,part):
        part = str(part)
        if self.text == "":
             self.text = part
        else:
            self.text = self.text + " " + part


    def uppercase(self):
        return self.text.upper()


    def clear(self):
       self.text = ""


    def get_text(self):
       return self.text




test_line = TestLine("Text")
print(test_line.uppercase())
test_line.clear()
print(test_line.get_text())


# Задача 10 — Понимание self
# Создай класс Clicker.
# В __init__(self) заведи атрибут count = 0.
# Добавь методы:
# click() — увеличивает count на 1.
# reset() — обнуляет count.
# get_count() — возвращает текущее значение count.
# Проверь: создай два объекта, у каждого сделай разное число кликов — значения должны быть независимыми.
# Готов проверить. Если нужна подсказка — напиши “дай подсказку”.
# Подтвердил корректность предыдущего решения
# Выдал следующую простую задачу без кода


class Clicker:

    def __init__(self,count=0):
        self.count = count


    def click(self):
         self.count += 1


    def reset(self):
        self.count = 0


    def get_count(self):
        return self.count


clicker = Clicker()
clicker.click()
clicker.click()
clicker.reset()
print(clicker.get_count())
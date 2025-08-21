# Задача 1 — Наследование и переопределение
# Создай базовый класс Animal с __init__(self, name) и методом sound(self), который возвращает строку "Звук".
# Создай класс Dog(Animal), который переопределяет метод sound(self), чтобы он возвращал "Гав".
# Создай объект Dog("Шарик"), проверь: sound() возвращает "Гав", атрибут name равен "Шарик".
# Дополнительно: создай Cat(Animal) с sound() → "Мяу".



class Animal:


    def __init__(self,name):
        self.name = name


    def sound(self):
        return "Звук"


class Dog(Animal):


    def sound(self):
        return "Гав"


class Cat(Animal):


    def sound(self):
        return "Мяу"


dog = Dog("Шарик")
print(dog.sound())
cat = Cat("Маруся")
print(cat.sound())
animal = Animal("Животное")
print(animal.sound())


# Задача 2 — Расширение конструктора через super()
# Создай базовый класс Vehicle с __init__(self, brand) и атрибутом brand.
# Создай класс Car(Vehicle):
# В __init__(self, brand, seats) сначала вызови родительский __init__ через super(), затем сохрани seats.
# Добавь метод info(self), который возвращает строку: "Brand: [brand], Seats: [seats]".
# Проверь: создай Car("Toyota", 5), убедись, что brand унаследован и info() возвращает корректную строку.
# Напиши “проверь” со своим решением или “дай подсказку”, если застрял.
# Выдал задачу по наследованию с использованием super() без решений.

class Vehicle:


    def __init__(self,brand):
        self.brand = brand


class Car(Vehicle):


    def __init__(self,brand,seats):
        super().__init__(brand)
        self.seats = seats


    def info(self):
        return f"Brand: {self.brand}, Seats: {self.seats}"


car = Car("Toyota",5)
print(car.info())


# Задача 3 — Переопределение метода с вызовом super()
# Создай базовый класс User с __init__(self, name) и методом describe(self), возвращающим строку: "User: [name]".
# Создай класс Admin(User):
# В __init__(self, name, level) вызови родительский конструктор и сохрани level.
# Переопредели describe(self), чтобы он использовал результат super().describe() и добавлял ", Level: [level]".
# Проверь: объект Admin("Анна", 3) — describe() возвращает строку с именем и уровнем.

class User:


    def __init__(self, name):
        self.name = name


    def describe(self):
        return f"User: {self.name}"


class Admin(User):


    def __init__(self,name,level):
        super().__init__(name)
        self.level = level


    def describe(self):
        user_name =super().describe()
        return f"{user_name}, Level: {self.level}"


user = User("Anna")
print(user.describe())

admin = Admin("Anna",5)
print(admin.describe())


# Задача 4 — Проверка наследования (isinstance/issubclass)
# Создай базовый класс Vehicle.
# Создай класс Bike(Vehicle).
# Создай объекты: v = Vehicle(), b = Bike().
# Проверь и выведи результаты:
# isinstance(v, Vehicle)
# isinstance(b, Vehicle)
# isinstance(v, Bike)
# isinstance(b, Bike)
# issubclass(Bike, Vehicle)
# issubclass(Vehicle, Bike)
# Ожидаются логические значения в соответствии с наследованием.

class Vehicle:
    pass


class Bike(Vehicle):
    pass



v = Vehicle()
b = Bike()
print(isinstance(v,Vehicle))
print(isinstance(b,Vehicle))
print(isinstance(v,Bike))
print(isinstance(b,Bike))
print(issubclass(Bike,Vehicle))
print(issubclass(Vehicle,Bike))

# Задача 5 — Наследование: расширение возможностей
# Создай базовый класс Account с __init__(self, owner, balance=0) и методом deposit(self, amount), который увеличивает баланс.
# Создай класс PremiumAccount(Account), который добавляет метод gift(self), повышающий баланс на 100.
# Проверь:
# У обычного аккаунта работает deposit, но нет gift.
# У премиум аккаунта работают и deposit, и gift.
# Балансы изменяются корректно.

class Account:


    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
          self.balance += amount


class PremiumAccount(Account):

    def gift(self):
        self.balance += 100


account = Account("Счетовод")
account.deposit(25)
print(account.balance)
premium_account = PremiumAccount("Premka")
premium_account.deposit(54)
premium_account.gift()
print(premium_account.balance)


# Задача 6 — Многоуровневое наследование и super()
# Создай класс LivingBeing с __init__(self, name) — сохраняй name.
# Создай класс Mammal(LivingBeing):
# В __init__(self, name) вызови родительский конструктор.
# Добавь атрибут has_fur = True.
# Создай класс Dog(Mammal):
# В __init__(self, name, breed) вызови конструктор Mammal.
# Сохрани breed.
# Проверь:
# Dog("Шарик", "Ovcharka") имеет name, breed, has_fur == True.
# Все конструкторы вызываются корректно через super().

class LivingBeing:


    def __init__(self,name):
        self.name = name


class Mammal(LivingBeing):


    def __init__(self,name):
        super().__init__(name)
        self.has_fur = True


class Dog(Mammal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Шарик","Овчарка")
assert dog.has_fur
print(dog.name,dog.breed,dog.has_fur)


# Задача 7 — Наследование: новый метод + super в методе
# Создай базовый класс Person с __init__(self, name) и методом greet(self), который возвращает строку: "Привет, [name]".
# Создай класс Student(Person) с __init__(self, name, group), сохрани group.
# В Student добавь метод introduce(self), который использует результат super().greet() и добавляет: ", я из группы [group]".
# Проверь: для Student("Иван", "A1") метод introduce() должен возвращать корректную строку; greet() тоже должен работать.
# Напиши “проверь” со своим решением или “дай подсказку”.


class Person:


    def __init__(self,name):
        self.name = name


    def greet(self):
        return f"Привет, {self.name}"


class Student(Person):


    def __init__(self,name,group):
        super().__init__(name)
        self.group = group


    def introduce(self):
        greeting = super().greet()
        return f"{greeting}, я из группы {self.group}"


students = Student("Иван","A1")
print(students.introduce())
print(students.greet())

# Задача 8 — Наследование: расширение поведения
# Создай базовый класс Account с __init__(self, owner, balance=0) и методом deposit(self, amount) — увеличивает баланс.
# Создай класс SavingsAccount(Account) с дополнительным атрибутом interest_rate (в процентах).
# Добавь метод apply_interest(self), который увеличивает текущий баланс на процент interest_rate.
# Проверь: внеси депозит, затем примени проценты — баланс должен увеличиться.


class Account:


    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        return self.balance


class SavingAccount(Account):


    def __init__(self,owner,interest_rate,balance=0):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate


    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate // 100)
        return self.balance


acc = Account("Lilo",200)
print(acc.deposit(11))

saving = SavingAccount("Lilo",15,100)
print(saving.apply_interest())


# Задача 9 — Наследование с доинициализацией и переопределением метода
# Создай базовый класс Product с __init__(self, name, price) и методом info(self),
# возвращающим строку: "Name: [name], Price: [price]".
# Создай класс DiscountProduct(Product) с __init__(self, name, price, discount_percent).
# Вызови super() и сохрани скидку.
# Добавь метод get_price(self), который возвращает цену с учётом скидки (в процентах).
# Переопредели info(self): используй результат
# super().info() и добавь ", Discount: [discount_percent]%, Final: [цена_со_скидкой]".
# Проверь на одном объекте: что возвращает get_price() и info().
# Скажи “дай подсказку” (без кода) или “проверь” — проверю твоё решение.

class Product:


    def __init__(self,name,price):
        self.name = name
        self.price = price


    def info(self):
        return f"Name: {self.name}, Price: {self.price:.2f}"


class DiscountProduct(Product):
    def __init__(self,name,price,discount_percent):
        super().__init__(name,price)
        self.discount_percent = discount_percent


    def get_price(self):
        return round(self.price * (1 - self.discount_percent / 100),2)


    def info(self):
        base_info = super().info()
        final_price = self.get_price()
        return f"{base_info}, Sale: {self.discount_percent}%, Final: {final_price:.2f}"



product = Product("Samsung", 1000)
print(product.name)
print(product.info())


discount = DiscountProduct("Samsung",1000,20)
print(discount.get_price())
print(discount.discount_percent)
print(discount.info())


# Задача 10 — Наследование с переопределением и super() в конструкторе
# Создай базовый класс Product с __init__(self, name) и методом info(self), возвращающим строку: "Product: [name]".
# Создай класс Book(Product):
# В __init__(self, name, author) вызови родительский конструктор через super() и сохрани author.
# Переопредели info(self), чтобы использовать super().info() и добавить ", Author: [author]".
# Добавь метод get_author(self), который возвращает автора.
# Проверь: создай Book("Война и мир", "Толстой"), вызови info() и get_author().

class Product:


    def __init__(self,name):
        self.name = name


    def info(self):
        return f"Product: {self.name}"


class Book(Product):


    def __init__(self,name,author):
        super().__init__(name)
        self.author = author


    def get_author(self):
        return self.author


    def info(self):
        base_info = super().info()
        return f"{base_info}, Author: {self.author}"


book = Book("Война и мир", "Толстой")
print(book.info())
print(book.get_author())



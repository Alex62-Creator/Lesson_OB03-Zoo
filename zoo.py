# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для
# `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и
# сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle

class Animal():
    def __init__(self, name, sound, eat):
        self.name = name
        self.sound = sound
        self.eat = eat

    def get_name(self):
        return self.name

    def func_sound(self):
        pass

    def func_eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, sound, eat):
        super().__init__(name, sound, eat)
        self.move = "Умеет летать"

    def func_sound(self):
        return self.sound

    def func_eat(self):
        return self.eat

class Mammal(Animal):
    def __init__(self, name, sound, eat):
        super().__init__(name, sound, eat)
        self.move = "Умеет бегать"

    def func_sound(self):
        return self.sound

    def func_eat(self):
        return self.eat

class Replite(Animal):
    def __init__(self, name, sound, eat):
        super().__init__(name, sound, eat)
        self.move = "Умеет ползать"

    def func_sound(self):
        return self.sound

    def func_eat(self):
        return self.eat

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.get_name()} умеет {animal.func_sound()} и любит {animal.func_eat()}")

animals = [Bird("Воробей", "чирикать", "семечки"), Mammal("Тигр", "рычать", "мясо"), Replite("Змея", "шипеть", "мышей")]

animal_sound(animals)

class Zoo():
    def __init__(self):
        self.animal_list = []
        self.employee_list = []

    def add_animal(self, id, name, sound, eat):
        match id:
            case "п":
                animal = Bird(name, sound, eat)
            case "м":
                animal = Mammal(name, sound, eat)
            case "р":
                animal = Replite(name, sound, eat)
            case _:
                print("Неопознанный вид животного")
        self.animal_list.append(animal)

    def print_animals(self):
        for animal in self.animal_list:
            print(f"{animal.get_name()} умеет {animal.func_sound()} и любит {animal.func_eat()}")

    def add_employee(self, id, name, age):
        match id:
            case "с":
                employee = ZooKeeper(name, age)
            case "в":
                employee = Veterinarian(name, age)
            case _:
                print("Нет такой категории работников")
        self.employee_list.append(employee)

    def print_employees(self):
        for employee in self.employee_list:
            print(f"{employee.name} {employee.age} лет. В его обязанности входит {employee.duty}")

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.duty = "кормить животных"

    def feed_animal(self):
        print("Кормит животных")

class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.duty = "лечить животных"

    def heal_animal(self):
        print("Лечит животных")

try:
    with open("zoo_list.txt", "rb") as f:
        zoo = pickle.load(f)
except EOFError:
    zoo = Zoo()

zoo.add_animal("п", "Петух", "кукарекать", "зерно")
zoo.add_animal("м","Кот", "мяукать", "молоко")
zoo.add_animal("р","Кобра", "шипеть", "лягушек")

zoo.print_animals()

zoo.add_employee("в", "Иван", "35")
zoo.add_employee("с", "Пётр", "45")

zoo.print_employees()

with open("zoo_list.txt", "wb") as f:
    pickle.dump(zoo, f)
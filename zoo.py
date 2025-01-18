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

import pickle           # Используем для сохранения объекта класса Zoo в файле

# Базовый класс для животных
class Animal():
    def __init__(self, name, age, sound, eat):
        self.name = name                # Имя животного
        self.age = age                  # Возраст животного
        self.sound = sound              # Издаваемые звуки
        self.eat = eat                  # Потребляемая пища

    def get_name(self):                 # Получаем имя животного
        return self.name

    def get_age(self):                 # Получаем возраст животного
        return self.age

    def func_sound(self):               # Получаем звуки животного. Будет переопределена
        pass

    def func_eat(self):                 # Получаем потребляемую пищу животным. Будет переопределена
        pass

# Дочерний класс Описывает птиц
class Bird(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound, eat) # Наследуем атрибуты базового класса
        self.move = "Умеет летать"              # Добавляем атрибут "движение"

    def func_sound(self):                       # Переопределяем функцию звуков
        return self.sound

    def func_eat(self):                         # Переопределяем функцию потребляемой пищи
        return self.eat

# Дочерний класс Описывает млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound, eat) # Наследуем атрибуты базового класса
        self.move = "Умеет бегать"              # Добавляем атрибут "движение"

    def func_sound(self):                       # Переопределяем функцию звуков
        return self.sound

    def func_eat(self):                         # Переопределяем функцию потребляемой пищи
        return self.eat

# Дочерний класс Описывает рептилий
class Replite(Animal):
    def __init__(self, name, age, sound, eat):
        super().__init__(name, age, sound, eat) # Наследуем атрибуты базового класса
        self.move = "Умеет ползать"             # Добавляем атрибут "движение"


    def func_sound(self):                       # Переопределяем функцию звуков
        return self.sound

    def func_eat(self):                         # Переопределяем функцию потребляемой пищи
        return self.eat

def animal_sound(animals):                      # Создаем функцию, которая принимает список животных и вызывает методы для каждого животного
    for animal in animals:
        print(f"{animal.get_name()} умеет {animal.func_sound()} и любит {animal.func_eat()}. Возраст {animal.get_age()} лет")

animals = [Bird("Воробей", "5", "чирикать", "семечки"), Mammal("Тигр", "10","рычать", "мясо"),
           Replite("Змея", "7", "шипеть", "мышей")]          # Создаем список животных разных классов

animal_sound(animals)                           # Вызываем функцию, демонстрирующую наследование и полиморфизм

# Класс объединяющий работников и животных Для связи классов используем композицию
class Zoo():
    def __init__(self):
        self.animal_list = []                   # Пустой список животных. Применяется если файл с информацией пустой
        self.employee_list = []                 # Пустой список работников. Применяется если файл с информацией пустой

    def add_animal(self, id, name, age, sound, eat): # Метод добавления животных в список
        match id:                               # Определяем вид животного
            case "п":
                animal = Bird(name, age, sound, eat)     # Птицы
            case "м":
                animal = Mammal(name, age, sound, eat)   # Млекопитающие
            case "р":
                animal = Replite(name, age, sound, eat)  # Рептилии
            case _:
                print("Неопознанный вид животного")
        self.animal_list.append(animal)

    def print_animals(self):                    # Метод вывода списка животных
        for animal in self.animal_list:
            print(f"{animal.get_name()} умеет {animal.func_sound()} и любит {animal.func_eat()}. Возраст {animal.get_age()} лет")

    def add_employee(self, id, name, age):      # Метод добавления работников в список
        match id:                               # Определяем специализацию работника
            case "с":
                employee = ZooKeeper(name, age)     # Смотритель
            case "в":
                employee = Veterinarian(name, age)  # Ветеринар
            case _:
                print("Нет такой категории работников")
        self.employee_list.append(employee)

    def print_employees(self):                  # Метод вывода списка работников
        for employee in self.employee_list:
            print(f"{employee.name} {employee.age} лет. В его обязанности входит {employee.duty}")

# Базовый класс для работников
class Employee():
    def __init__(self, name, age):
        self.name = name                        # Имя работника
        self.age = age                          # Возраст работника

# Дочерний класс Описывает смотрителей
class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)             # Наследуем атрибуты базового класса
        self.duty = "кормить животных"          # Добавляем атрибут "обязанности"

    def feed_animal(self):                      # Специфический метод в классе ZooKeeper
        print("Кормит животных")

# Дочерний класс Описывает ветеринаров
class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)             # Наследуем атрибуты базового класса
        self.duty = "лечить животных"           # Добавляем атрибут "обязанности"

    def heal_animal(self):                      # Специфический метод в классе Veterinarian
        print("Лечит животных")

try:
    with open("zoo_list.txt", "rb") as f:       # Считываем сохраненный в файле объект Zoo
        zoo = pickle.load(f)
except EOFError:                                # Если файл пустой, создаем новый объект Zoo
    zoo = Zoo()

# Добавляем новые объекты производных классов от Animal
zoo.add_animal("п", "Петух", "5", "кукарекать", "зерно")
zoo.add_animal("м","Кот", "10", "мяукать", "молоко")
zoo.add_animal("р","Кобра", "25", "шипеть", "лягушек")

zoo.print_animals()                             # Печатаем список животных

# Добавляем новые объекты производных классов от Employee
zoo.add_employee("в", "Иван", "35")
zoo.add_employee("с", "Пётр", "45")

zoo.print_employees()                           # Печатаем список работников

with open("zoo_list.txt", "wb") as f:           # Записываем объект Zoo в файл
    pickle.dump(zoo, f)
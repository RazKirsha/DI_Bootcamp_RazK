class Animal():
    def __init__(self):
        self.legs = 4
        self.name = "Bob"


animal = Animal()
print(animal.legs)
print(animal.name)


class Animal2():
    def __init__(self, legs, name):
        self.legs = legs
        self.name = name

    def add_height(self, height):
        self.height = height
        print(f'This is my height: {self.height}m')


animal2 = Animal2(6, 'Oded')
print(animal2.legs)
print(animal2.name)

print(isinstance(animal2, Animal2))
print(isinstance('animal2', Animal2))

animal2.add_height(1.80)

print('NEXT CLASS')


class Car():
    def __init__(self, color, brand, model, speed):
        self.color = color
        self.brand = brand
        self.model_name = model
        self.top_speed = speed
        self.print_speed()

    def print_speed(self):
        print(f'Your top speed is: {self.top_speed}')

    def __str__(self):
        return f'This is the brand: {self.brand}'

    def __gt__(self, other):
        # __gt__ is short for greater than!
        if isinstance(other, Car):
            return self.top_speed > other.top_speed
        elif isinstance(other, int):
            return self.top_speed > other


my_car = Car('Red', 'Mazda', 'Mazda 2', 250)
# After my_car was created, it is initializing self.print_speed()
print(my_car.color)
print(my_car.brand)
print(my_car.model_name)
print(my_car.top_speed)
print(my_car)
print('SETTING ANOTHER CAR')
other_car = Car('yellow', 'Toyota', 'Corola', 200)
print(other_car)
# Asking if my_car.top_speed is greater than other_car.top_speed (lines 48-53)
# Going to the first if statement because this is a Car class (lines 50-51)
# returns True (250 > 200)
print(my_car > other_car)
# Going to the elif statement because this is an integer (lines 52-53)
# returns False (250 < 400)
print(my_car > 400)

# Way1 of import function from another file: CN2
import CN2

CN2.say_hello('Raz')

# Way2 of import function from another file
from CN2 import say_hello

say_hello('Bla')

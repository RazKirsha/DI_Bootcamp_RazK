# Ex1
# print('----------------Ex1------------------')
#
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Javanese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# cat1 = Bengal('Mitzi', 1)
# cat2 = Chartreux('Kitzi', 2)
# cat3 = Javanese('Yitzi', 3)
# my_cats = [cat1, cat2, cat3]
# my_pets = Pets(my_cats)
# my_pets.walk()

# Ex2
# print('----------------Ex2------------------')


class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        dog1_stats = self.weight * self.run_speed()
        dog2_stats = other_dog.weight * other_dog.run_speed()
        if dog1_stats > dog2_stats:
            return self.name
        return other_dog.name


dog1 = Dog('Mike', 10, 30)
dog2 = Dog('Rike', 12, 25)
dog3 = Dog('Bike', 9, 35)
# print(dog1.run_speed())
# print(dog2.run_speed())
# print(dog3.run_speed())
# print(dog1.fight(dog2))
# print(dog1.fight(dog3))
# print(dog2.fight(dog3))
#
# # Ex3
# print('----------------Ex3------------------')

# Ex1
from math import pi
import random


class Circle:

    def __init__(self, radius=1.0):
        self.radius = radius
        self.paramiter = 2 * pi * radius
        self.area = pi * (radius ** 2)

    def __str__(self):
        return "A circle is a round shaped figure that has no corners or edges."


c = Circle(10)
print(c.radius)
print(c.paramiter)
print(c.area)
print(c)


# Ex 2

class myList:
    def __init__(self, lst):
        self.lst = lst
        self.rev = lst[::-1]
        self.srt = sorted(lst)

    def random_list(self):
        random_list = [random.randint(0, 1000) for num in self.lst]
        return random_list


a_list = [2, 4, 6, 1, 23, 95, 21, 35, 11, 19]
new_list = myList(a_list)
print(new_list.rev)
print(new_list.srt)
print(new_list.random_list())

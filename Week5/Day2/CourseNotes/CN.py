class Animal:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def make_noise(self):
        print('AH!')

    def walk(self):
        print(f'{self.name} is walking')


class Dog(Animal):
    def __init__(self, name, boy_or_girl, age, a_type):
        # to get all attributes from parent class (Animal)
        super().__init__(name, boy_or_girl, age)
        # adding another attribute to the dog class
        self.type = a_type

    def make_noise(self):
        # Takes the function "make_noise" from the parent class (Animal)
        super().make_noise()
        # Adds on top of the function some more
        print(f'{self.name} Says WOOF!')

    def fetch_ball(self):
        print(f'{self.name} Goes to get the ball!')


a1 = Animal('Mitzi', 'girl', 4)
d1 = Dog('Rocky', 'boy', 2, 'Bulldog')
print('This is a1 - Animal class')
print(a1.name)
print(a1.sex)
print(a1.age)
a1.make_noise()
print('This is d1 - Dog class')
print(d1.name)
print(d1.sex)
print(d1.age)
print(d1.type)
d1.make_noise()
d1.walk()
d1.fetch_ball()

my_list = [2, 3, '1', 2, 'Four', 42, 1, 5, 3, 'I_am_a_number']


def sum_malicious(given_list):
    sum = 0
    for num in given_list:
        try:
            sum += float(num)
        except TypeError and ValueError:
            pass
    return sum


print(sum_malicious(my_list))

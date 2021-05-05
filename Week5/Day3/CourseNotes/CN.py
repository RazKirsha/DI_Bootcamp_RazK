from random import choice


class Animal:
    animal_list = []

    def __init__(self, name, age=2):
        self.name = name
        self.age = age
        self.animal_list.append(self)

    def sleep(self):
        print('zzzZZZzzz')

    def __repr__(self):
        return f'Im an animal named {self.name}'

    def __str__(self):
        return f'Hey, Im an animal named {self.name}'

    def __len__(self):
        return len(Animal.animal_list)

    def __add__(self, other_dog):
        combined_ages = self.age + other_dog.age
        return combined_ages

    def __call__(self):
        return 'Hi Im an animal being called'

    def __gt__(self, other):
        return self.age > other.age


class Dog(Animal):
    def bark(self):
        print(f'{self.name} barked, WAF!')

    def __repr__(self):
        return f'Im a dog named {self.name}'

    def __str__(self):
        return f'Hey, Im a dog named {self.name}'


age_demo = 1
for name in ['toby', 'matthew', 'sparky']:
    # randomly choosing between Dog class ot Animal class
    current_class = choice([Dog, Animal])
    current_class(name, age_demo)
    age_demo += 1

print(Animal.animal_list)
animal = Animal.animal_list[0]
animal2 = Animal.animal_list[1]
print(animal)
# this is 3 because of toby, matthew and sparky
print(len(animal))
print(f'animal1 age: {animal.age}')
print(f'animal2 age: {animal2.age}')
print(f'combined ages: {animal + animal2}')
print(animal2 > animal)
print(animal())

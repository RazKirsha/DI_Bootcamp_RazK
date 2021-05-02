# Ex1
class Cat:
    all_cats = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.all_cats.append(self)


cat1 = Cat('Napkin', 3)
cat2 = Cat('Bob', 1)
cat3 = Cat('Malanie', 5)

for cat in Cat.all_cats:
    oldest_cat_name = ''
    oldest_cat_age = 0
    if cat.age > oldest_cat_age:
        oldest_cat_name = cat.name
        oldest_cat_age = cat.age

print(f'The oldest cat is {oldest_cat_name}, and is {oldest_cat_age} years old')


# Ex2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2}cm high')


davids_dog = Dog('Rex', 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is higher')
elif sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is higher')


# Ex3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Ex4

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.dictionary = {}
        self.name = zoo_name

    def new_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(self.animals)

    def get_animals(self):
        print(self.animals)

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        key = 1
        new_letter = []
        self.animals.sort()
        self.animals.append(' ')
        for index, animal in enumerate(self.animals):
            if index != len(self.animals) - 1:
                if self.animals[index][0] != self.animals[index + 1][0]:
                    new_letter.append(animal)
                    self.dictionary[key] = new_letter
                    key += 1
                    new_letter = []
                else:
                    new_letter.append(animal)
        print(self.dictionary)

    def get_groups(self, index):
        if index not in self.dictionary.keys():
            print('enter another index')
        else:
            print(self.dictionary[index])


new_zoo = Zoo('ramat_gan_safari')
new_zoo.new_animal('Ape')
new_zoo.new_animal('Eel')
new_zoo.new_animal('Cougar')
new_zoo.new_animal('Bear')
new_zoo.new_animal('Baboon')
print(new_zoo.sort_animals())
new_zoo.get_groups(2)

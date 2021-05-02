class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
        self.animal_list = []

    def add_animal(self, animal, amount=1):
        if animal not in self.animals:
            self.animals[animal] = amount
        else:
            self.animals[animal] += amount

    def get_info(self):
        print(f"{self.name}'s farm")
        for key, value in self.animals.items():
            print(key + ' : ' + str(value))
        print('E-I-E-I-O!')

    def get_animal_types(self):
        for animal in self.animals.keys():
            self.animal_list.append(animal)
        self.animal_list.sort()
        print(self.animal_list)

    def get_short_info(self):
        print(f"{self.name}'s farm has {self.animal_list} ")


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_animal_types()
macdonald.get_short_info()
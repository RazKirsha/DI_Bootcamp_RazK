import regXP
import random


class PetDog(regXP.Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        print(super().bark())

    def play(self, *dog_names):
        print(f'{dog_names} all play together')

    def do_a_trick(self):
        tricks = [' does a barrel roll', ' stands on his back legs', ' shakes you hand', ' plays dead']
        if self.trained:
            print(self.name + random.choice(tricks))


dog4 = PetDog('Shike', 5, 15)
dog4.train()
print(dog4.trained)
dog1 = regXP.Dog('Mike', 10, 30)
dog2 = regXP.Dog('Rike', 12, 25)
dog3 = regXP.Dog('Bike', 9, 35)
dog4.play(dog1.name, dog2.name, dog3.name)
dog4.do_a_trick()
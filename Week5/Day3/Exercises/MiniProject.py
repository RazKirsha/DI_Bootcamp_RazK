class Character:

    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        if isinstance(other, Character):
            other.life -= 1
            self.attack -= 1

class Druid(Character):

    def meditate(self):
        print('Now Meditates')
        self.attack -= 2
        self.life += 10

    def animal_help(self):
        print('Helping an animal')
        self.attack += 5

    def fight(self, other):
        if isinstance(other, Character):
            other.life -= (0.75 * (self.life + self.attack))

class Warrior(Character):

    def brawl(self, other):
        if isinstance(other, Character):
            other.life -= 2 * self.attack
            self.life += 0.5 * self.attack

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, other):
        if isinstance(other, Character):
            other.attack -= 3


class Mage(Character):

    def curse(self, other):
        if isinstance(other, Character):
            other.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other):
        if isinstance(other, Character):
            other.life -= int(self.attack/self.life)


druid1 = Druid('drod')
warrior1 = Warrior('kratos')
mage1 = Mage('Merlin')

druid1.animal_help()
print(druid1.life)
print(druid1.attack)
druid1.meditate()
print(druid1.life)
print(druid1.attack)
druid1.basic_attack(mage1)
print(druid1.life)
print(druid1.attack)
print(mage1.life)
print(mage1.attack)
import random
import datetime

# Ex1

print('-----------Ex1-----------')

today = datetime.date.today()
print(today)

# Ex2
print('-----------Ex2-----------')
now = datetime.datetime.now()
happy_new_year = datetime.datetime(today.year + 1, 1, 1, 0, 0, 0)
print(f'New year\'s eve will be in: {happy_new_year - now}')

# Ex3
print('-----------Ex3-----------')

# birth_year = int(input('Enter your birth year: '))
# birth_month = int(input('Enter your birth month: '))
# birth_day = int(input('Enter your birth day: '))
#
# birthday = datetime.date(birth_year, birth_month, birth_day)
#
# age = today - birthday
# age_in_minutes = age.days
# print(f'{age_in_minutes * 24 * 60} Minutes old')

# Ex4
print('-----------Ex4-----------')


def holiday():
    upcoming_holiday = datetime.datetime(2021, 5, 10)
    right_now = datetime.datetime.now()
    print(right_now)

    print(f'Jerusalem\'s day is in {upcoming_holiday - right_now}')


holiday()

# Ex5
print('-----------Ex5-----------')


class Age_By_planet:

    def __init__(self, age_in_seconds):
        self.age_in_seconds = age_in_seconds
        self.age = ((((self.age_in_seconds / 365.25) / 24) / 60) / 60)
        self.planet = {
            'Mercury': 0.2408467,
            'Venus': 0.61519726,
            'Mars': 1.8808158,
            'Jupiter': 11.862615,
            'Saturn': 29.447498,
            'Uranus': 84.016846,
            'Neptune': 164.79132
        }

    def age_on_planet(self, planet):
        if planet in self.planet:
            planet_age = self.age / self.planet[planet]
            return planet_age


my_age = Age_By_planet(1000000000)
print(my_age.age)
print(my_age.age_on_planet('Mercury'))

# Ex6
print('-----------Ex6-----------')
from faker import Faker

users = []


def add_new_user():
    code_languages = ['Python', 'Javascript', 'Java', 'C#', 'Assembler', 'Visual Basic']
    fake = Faker()
    new_user = {
        'name': fake.name(),
        'address': fake.address(),
        'code language': random.choice(code_languages)
    }

    return new_user


for user in range(10):
    users.append(add_new_user())

print(users)

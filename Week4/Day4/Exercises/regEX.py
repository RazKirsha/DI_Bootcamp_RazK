# Ex1
def display_message():
    print("I'm learning at DI!!")

display_message()

# Ex2
def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Percy Jackson')

# Ex3
def describe_city(city = 'Holon', country = 'Israel'):
    print(f'{city} is in {country}')

describe_city()

# Ex4
import random
def random_num(num):
    num2 = random.randint(1, 101)
    if num == num2:
        print("GREAT SUCCESS")
    else:
        print(f''' 
        num1 = {num} \n
        num2 = {num2}
        ''')

random_num(14)

# Ex5
def make_shirt(size = 'L', text = 'I Love python'):
    print(f'shirt size is {size} \n text on shirt is {text}')

make_shirt('XL','Avengers')
make_shirt()
make_shirt('M')
make_shirt(text = 'Avengers')

# Ex6
magicians = ['Houdini', 'Chicko', 'Dicko', 'Hezi Din']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for magician in magicians:
        print(f'The great {magician}')

show_magicians(magicians)
make_great(magicians)
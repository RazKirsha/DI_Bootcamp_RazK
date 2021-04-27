my_fav_numbers = {19, 10, 23, 7, 4}
my_fav_numbers.add(99)
my_fav_numbers.add(77)
print(my_fav_numbers)

my_fav_numbers.remove((max(my_fav_numbers)))
print(my_fav_numbers)

friend_fav_numbers = {11, 33, 22}

our_fav_numbers = set()
our_fav_numbers.update(my_fav_numbers)
our_fav_numbers.update(friend_fav_numbers)
print(our_fav_numbers)

for i in range(21):
    print(i)

# Floats
j = 1.5
for i in range(8):
    print(j)
    j += 0.5

# Shopping List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
print(basket)

basket.pop()
print(basket)

basket.append('Kiwi')
print(basket)

basket.insert(0,'Apples')
print(basket)

print(len(basket))

# print(basket.count['Apples'])

basket = []

print(basket)

# Loop
name = input('Enter Your name: \n')
while name.title() != 'Raz':
    name = input('Enter my name: \n')

# Exercise 7
listush = [4, 7, 4, 9, 4, 67, 8, 35, 7, 85, 'qw']
for index,argu in enumerate(listush):
    if index%2==0:
        print(argu)

# Exercise 8
for i in range(1500, 2500):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

# Favorite Fruits
fav_fruits = []
new_fruit = input('Enter Your Favourite fruits one by one. To stop write "stop"')
while new_fruit.lower() != 'stop':
    fav_fruits.append(new_fruit)
    new_fruit = input('Enter Your Favourite fruits one by one. To stop write "stop"')

named_fruit = input('Enter a name of a fruit')

if named_fruit in fav_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')

# Who Ordered A Pizza ?
topping = input('Enter a topping. to stop write "stop"')
all_topping = []
price = 10
while topping != 'stop' or topping != 'none':
    print(f'{topping} has been added to your pizza!')
    price += 2.5
    all_topping.append(topping)
    topping = input('Enter a topping. to stop write "stop"')

print(f'Your toppings are: \n {all_topping}')
print(f'Your price is {price}')
price = 0

family_count = int(input("How many are you?: \n"))
for member in range(family_count):
    age = int(input("Enter your age:"))
    if 3 <= age < 12:
        price += 10
    elif age >= 12:
        price += 15

print(f'Total cost: {price}')

premitted_index = []
teens_count = int(input("How many are you?: \n"))
all_names = []
for member in range(teens_count):
    name = input('What is your name? \n')
    all_names.append(name)
    all_ages = []
    age = int(input('How old are you?'))
    if 16 <= age <= 21:
        premitted_index.append(member)

for i in premitted_index:
    print(f'{all_names[i]} Can go in')


# Who Is Under 16?
teens_count = int(input("How many are you?: \n"))
all_names = []
for member in range(teens_count):
    name = input('What is your name? \n')
    all_names.append(name)
    all_ages = []
    age = int(input('How old are you?'))
    if age < 16:
        all_names.pop()

print(all_names)

# Exercise 13
sandwich_orders = ['Pastrami', 'Cream Cheese', 'Pastrami', 'Nuttella', 'Omlette', 'Pastrami', 'Tuna']
finished_sandwiches = []
print('Ran out of pastrami')

for sandwich in sandwich_orders:
    if sandwich == 'Pastrami':
        sandwich_orders.remove(sandwich)
    else:
        finished_sandwiches.append(sandwich)
        print(f'I made your {sandwich} sandwich')

print(sandwich_orders)

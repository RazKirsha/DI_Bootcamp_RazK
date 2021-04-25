# Hello world
print("Hello World \n" * 5)
# Some Math
print((99**3)*8)

# What is the output?

print(5 < 3)
# False

print(3 == 3)
# True

# print("3" > 3)
# Error

print("Hello" == "hello")
# False

# Your computer brand
computer_brand = 'Dell'
print(f'I have a {computer_brand} computer')

# Your Information
name = 'Raz'
age = 23
shoe_size = 41
info = (f'Hey my name is {name}, {age} years old. My shoe size is {shoe_size}.')
print(info)

# A & B
a = 86
b = 62

if a > b:
    print("Hello World")

# Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print('Number is even!')
else:
    print('Number is odd!')

# What is your name
name = input("Enter your name: ")
if name.title() == 'Raz':
    "We Have the same name!!"
else:
    "Not as nice as Raz, But cool name though.."

# Tall enough to ride a roller coaster
height = int(input("Write your height in cm: "))
if height >= 145:
    print("Tall enough to ride!")
else:
    print("You need to grow some more to ride")

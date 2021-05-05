# f = open('secrets.txt', mode='w')
# f.write('This is a new line')
# f.close()
# print(secret_data)

# reading the data from the file and saving it to data argument
# with open('secrets.txt', 'r') as f:
#     data = f.read()


# adds another line to the data argument
# with open('secrets.txt', 'w') as f:
#     f.write(data + '\nThis is a new line 22222')
#
# # reads the content of the file
# with open('secrets.txt', 'r') as f:
#     data2 = f.read()
#
# print(data2)

import json

# with open('json_test.txt', 'r') as f:
#     # load is like read from json file as a python data type
#     json_dict = json.load(f)
#     # json.loads(f.read()) would be a string
#
# print(json_dict)
# # reads it as a dictionary
# print(type(json_dict))


# my_family = {
#     "parents": ['Beth', 'Jerry'],
#     "children": ['Summer', 'Morty']
# }
#
#
# def write_to_json(data):
#     with open('new_json.json', 'w') as f:
#         json.dump(data, f)
#
#
# def read_from_json():
#     with open('new_json.json', 'r') as f:
#         data = json.load(f)
#     return data
#
#
# write_to_json(my_family)
# new_fam = read_from_json()
# print(new_fam)
#
# new_fam['JSONTest'] = 'Hello world'
# write_to_json(new_fam)
# print(read_from_json())


# def add_item_to_menu(name, price):
#     menu.append({'name': name,
#                  'price': price})
#
#
# def read_from_menu():
#     with open('menu.json', 'r') as f:
#         data = json.load(f)
#     return data
#
#
# try:
#     menu = read_from_menu()
# except FileNotFoundError and json.decoder.JSONDecodeError:
#     menu = []
#
#
# def write_to_menu(data):
#     with open('menu.json', 'w') as f:
#         json.dump(data, f)
#
#
# print(menu)
# while True:
#     name = input('Enter a name of a dish: ')
#     if name == 'quit':
#         break
#     price = input('Enter a price: ')
#     add_item_to_menu(name, price)
#
# print(menu)
# write_to_menu(menu)
import random

new_fam = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

with open('json2.json', 'w') as f:
    json.dump(new_fam, f)

with open('json2.json', 'r') as f:
    family = json.load(f)

for child in family['children']:
    print(f'{family["firstName"]}\'s child {child["firstName"]} is {child["age"]}')
    child['fav_color'] = random.choice(['blue', 'yellow', 'green'])

with open('json2.json', 'w') as f:
    json.dump(family, f, indent=2)

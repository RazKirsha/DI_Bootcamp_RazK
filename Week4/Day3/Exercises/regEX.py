# Ex1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
zipped_tuples = zip(keys, values)
dict = {}
for key, num in zipped_tuples:
    dict[key] = num

print(dict)

# Ex2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost = 0
for age in family.values():
    if 3 < age < 12:
        cost += 10
    elif age > 12:
        cost += 15

print(f'The total price is {cost}')

fam2 = {}
# name = input("What is your name? (To stop write 'stop'): ")
# age = int(input("How old are you? (To stop write '0'): "))
# cost = 0
# print(name)
# while name != 'stop':
#     fam2[name] = age
#     name = input("What is your name? (To stop write 'stop'): ")
#     age = int(input("How old are you? (To stop write '0'): "))
#     print(name)
#
# for age in fam2.values():
#     if 3 < age < 12:
#         cost += 10
#     elif age > 12:
#         cost += 15
#
# print(f'The total price is {cost}')

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2
print(brand)

for client in brand['type_of_clothes']:
    print(f'Zara client is: {client}')

brand['country_creation'] = 'Spain'
print(brand)

if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')
print(brand)

del brand['creation_date']
print(brand)

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand.keys()))

for val in brand.values():
    print(val)

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])

# Ex4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict1 = {}
dict2 = {}
dict3 = {}
new_users1 = []
new_users2 = []
dict1rec1 = {}
dict1rec2 = {}
for index, user in enumerate(users):
    dict1[user] = index
    dict2[index] = user

sorted_names = sorted(users)
for index, user in enumerate(sorted_names):
    dict3[user] = index

j = 0
k = 0
for user in users:
    if 'i' in user:
        dict1rec1[user] = j
        j += 1
    if user[0].lower() == 'p' or user[0].lower() == 'm':
        dict1rec2[user] = k
        k += 1

print(dict1)
print(dict2)
print(dict3)
print(dict1rec1)
print(dict1rec2)

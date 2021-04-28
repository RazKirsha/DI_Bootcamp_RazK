# sen = "Hello my name is RAZ"
# backward = sen[::-1]
# print(backward)

person_dict = {'age': 30, 'name': 'Bob', 'jobs': ['Coder', 'Engineer']}

# Grabbing 'age','name'...
for arg in person_dict:
    print(arg)
print('Break')

# Grabbing values -  3-, 'Bob'
for value in person_dict.values():
    print(value)
print('Break')

# Grabbing both as a tuple - ('age', 30)
for var in person_dict.items():
    print(var)
print('Break')

# Grabbing them separately - age 30
for key, value in person_dict.items():
    print(key, value)
print('Break')

# Searching for 'hello'
abc = person_dict.get('hello')
print(abc)
print('Break')

# Searching for 'hello', adn if does not exist print 'world'
abc = person_dict.get('hello', 'World')
print(abc)
print('Break')

# Adding 'skills' which is a dictionary to person_dict dictionary
person_dict['skills'] = {'python': 85, 'js': 100, 'pascal': 50}
print(person_dict)
# Grabbing 85 out of 'python'
print(person_dict['skills']['python'])
print('Break')

# Adding to skills a new list with key of 'java'
person_dict['skills']['java'] = [1, 2, 3]
print(person_dict)
# Grabbing the number 2 at index 1
print(person_dict['skills']['java'][1])
print('Break')

# Deleting 'age' key from person_dict
del person_dict['age']
print(person_dict)
print('Break')

# Merging two dicts to new_dict
new_dict = {'new': 'dict', 'testing': True}
new_dict.update(person_dict)
print(new_dict)
print('Break')


sampleDict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary", 'hello']

for KTR in keysToRemove:
    if KTR in sampleDict:
        del sampleDict[KTR]

print(sampleDict)

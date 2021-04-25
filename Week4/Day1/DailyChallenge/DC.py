import random
sen = input("Enter a sentence with exactly 10 characters \n")
while len(sen) != 10:
    if len(sen)<10:
        print('string not long enough')
    else:
        print('string too long')
    sen = input("Enter a sentence with exactly 10 characters \n")

print(sen[0])
print(sen[-1])
print("This is break")

string = ''
location = []
for letter in sen:
    string += letter
    print(string)

print("This is break")

mixed_sen = ''.join(random.sample(sen, len(sen)))
print(mixed_sen)

users = []
for i in range(3):
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    score = int(input('Enter score: '))
    tup = (name, age, score)
    users.append(tup)

# This is sorting by name first, then by age and then by score in reverse order
print(sorted(users, key=lambda x: (x[0], x[1], x[2]), reverse=True))

# add_three_lambda = lambda anything: anything + 3
# print(add_three_lambda(5))

# nums = range(1, 6)
# for num in nums:
#     square_it = lambda num: num ** 2
#     # print(square_it(num))
#
# print(map(square_it, nums))
# square_list = list(map(square_it, nums))
# print(square_list)

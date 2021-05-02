users_input = input('Enter a sequence of words separated by commas:\n')
unsorted_list = users_input.split(',')

sorted_list = [word for word in sorted(unsorted_list)]

print(sorted_list)
matrix = ['7i3', 'Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', '^r!']
complete_sen = ''
final = ''
old_line_index = 0
new_list = []
for index in range(3):
    for line in matrix:
        if line[index].isalpha():
            complete_sen += line[index]
        else:
            complete_sen += ' '


new_sen = complete_sen.split(' ')
for char in new_sen:
    if char.isalpha():
        new_list.append(char)


print(' '.join(new_list))

sen = input('Enter a sentence: ').split(' ')
longest_word = ''
newsen = []
stars1 = ''
stars2 = ''

for word in sen:
    if len(word) > len(longest_word):
        longest_word = word

for word in sen:
    while len(word) < len(longest_word):
        word += ' '
    newsen.append('* ' + word + ' *')

num_of_stars = len(longest_word)
stars1 = '*' * num_of_stars
stars2 = stars1
newsen.insert(0, stars1)
newsen.append(stars2)

for stared_word in newsen:
    print(stared_word)
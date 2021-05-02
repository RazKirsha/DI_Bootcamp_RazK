import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
print(word)

stars = []
for char in word:
    stars.append('*')

letter = 'AA'
tries = 6
used_letters = []
while '*' in stars and tries > 1 and letter not in used_letters or len(letter) != 1:
    letter = input('Enter a letter!')
    if letter not in word and len(letter) == 1:
        tries -= 1
        print('Wrong')
        print(f'Number of tries left: {tries}')
    else:
        for index, char in enumerate(word):
            if letter == word[index]:
                stars[index] = letter
                print(('').join(stars))

if tries <= 1:
    print('Fail!')
    print(f'The word was {word}')
if '*' not in stars:
    print('Winner!')
# How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velitesse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# Longest Word Without A Specific Character
playing = True
longestSen = 0
while playing == True:
    withoutA = input("Try to write the longest sentence without using 'A' ")
    withoutA = withoutA.lower()
    counter = 0
    for letter in withoutA:
        if letter != 'a':
            counter += 1
        else:
            break

    print(f'You managed to go {counter} times without "A"')
    if counter > longestSen:
        print(f'Congrats! You passed the last sentence by {counter - longestSen}! ')
        longestSen = counter
    elif counter == longestSen:
        print('You have matched the last record')
    else:
        print(f'You were {longestSen - counter} letters from the record!')
    print(counter)
    print(longestSen)
    print(counter)
    keepplaying = input("Want to keep try?")
    if keepplaying.lower() == 'no':
        playing = False

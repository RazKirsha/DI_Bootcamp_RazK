from AC import AnagramChecker

playing = True

print('Welcome to the Anagram Check!')
while playing:
    user_choice = ''
    print('Select one of the options below:')
    while user_choice != 'e' and user_choice != 'q':
        print('(e)nter an Anagram to test')
        print('(q)uit')
        user_choice = input('Enter your choice: ')
    if user_choice == 'e':
        user_word = input('Enter a word to see its anagrams: ').upper()
        test_word = AnagramChecker()
        result = test_word.is_anagram(user_word)
        if result == []:
            print('No anagrams for this word!')
        else:
            print('Those are the anagrams:')
            for word in result:
                print(word.lower())

    else:
        print('Bye Bye')
        playing = False
from game import Game

playing = True
results = {
    'win': 0,
    'loss': 0,
    'draw': 0
}
while playing:
    print('Welcome to Rock Paper Scissors!')
    users_menu_choice = ''
    while users_menu_choice != 'p' and users_menu_choice != 's' and users_menu_choice != 'q':
        print('What would you like to do?')
        print('(p)lay a new game')
        print('(s)how scores')
        print('(q)uit')
        users_menu_choice = input('Enter Choice: ')

    if users_menu_choice == 'p':
        game = Game.get_game_result()
        results[game] += 1
    elif users_menu_choice == 's':
        for key, value in results.items():
            print(f'{key} = {value}')
    else:
        print('Bye Bye')
        for key, value in results.items():
            results[key] = 0
        playing = False

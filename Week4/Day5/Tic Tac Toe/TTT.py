import random


def display_board(board):
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]}  ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]}  ')
    print('___|___|___')
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]}  ')
    print('   |   |   ')


def who_starts(user1, user2):
    num_user1 = 0
    num_user2 = 0

    while num_user1 == num_user2:
        num_user1 = random.randint(1, 10)
        num_user2 = random.randint(1, 10)

    if num_user1 > num_user2:
        print(f'{user1} starts!')
        starting = user1
        second = user2
    else:
        print(f'{user2} starts!')
        starting = user2
        second = user1

    return starting, second


def select_shape(starting_user, second_user):
    shape_startinguser = ''
    while shape_startinguser != 'X' and shape_startinguser != 'O':
        shape_startinguser = input(f'{starting_user} - Please Select a Shape (X/O): ')
    if shape_startinguser == 'X':
        shape_seconduser = 'O'
    elif shape_startinguser == 'O':
        shape_seconduser = 'X'

    print(f'{starting_user} Shape: {shape_startinguser} \n{second_user} Shape: {shape_seconduser}')
    return shape_startinguser, shape_seconduser


def player_input(board, location, usershape):
    board[location] = usershape
    print('New turn:')
    display_board(board)
    return board


def check_win(board, usershape):
    if board[1] == usershape and board[2] == usershape and board[3] == usershape:
        print('Win')
        return True
    elif board[4] == usershape and board[5] == usershape and board[6] == usershape:
        print('Win')
        return True
    elif board[7] == usershape and board[8] == usershape and board[9] == usershape:
        print('Win')
        return True
    elif board[1] == usershape and board[4] == usershape and board[7] == usershape:
        print('Win')
        return True
    elif board[2] == usershape and board[5] == usershape and board[8] == usershape:
        print('Win')
        return True
    elif board[3] == usershape and board[6] == usershape and board[9] == usershape:
        print('Win')
        return True
    elif board[1] == usershape and board[5] == usershape and board[9] == usershape:
        print('Win')
        return True
    elif board[3] == usershape and board[5] == usershape and board[7] == usershape:
        print('Win')
        return True
    else:
        return False


playing = True
while playing:
    turn = True
    while turn:

        # setting up the beginning of the game
        print("Welcome to Raz's Tic Tac Toe!!")
        board = ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # Setting up users and their shapes
        user1 = input('User1, Please enter your name: ')
        user2 = input('User2, Please enter your name: ')

        starting, second = who_starts(user1, user2)
        starting_shape, second_shape = select_shape(starting, second)

        keeping = True
        now_playing = starting
        shape = starting_shape
        while keeping:

            # Asking the user for a place
            used_places = []
            place = input(f'{now_playing} - Please enter the location of your {shape} (1-9): ')
            while True:
                if place.isnumeric():
                    if place not in used_places and int(place) >= 1 and int(place) <= 9:
                        break
                place = input(f'{now_playing} - Please enter the location of your {shape} (1-9): ')

            used_places.append(place)
            place = int(place)

            # placing the shape in the place
            player_input(board, place, shape)

            # check if there is a win
            if check_win(board, shape):
                print(f'{now_playing} is the WINNER!!!')
                keeping = False
                turn = False
                # asking if the user wanna play again
                again = input('Wanna play again?: ')
                if again[0].lower() == 'n':
                    playing = False
            # if the board is full
            elif ' ' not in board:
                print('No winner at this match!')
                keeping = False
                turn = False
                # asking if the user wanna play again
                again = input('Wanna play again?: ')
                if again[0].lower() == 'n':
                    playing = False
            # if the game continues, switch players
            else:
                if now_playing == starting:
                    now_playing = second
                    shape = second_shape
                elif now_playing == second:
                    now_playing = starting
                    shape = starting_shape

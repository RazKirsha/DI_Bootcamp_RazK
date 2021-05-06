import random


class Game:

    def __init__(self, points=0):
        self.points = points

    @staticmethod
    def get_user_item():
        user_item = ''
        while user_item != 'r' and user_item != 'p' and user_item != 's':
            user_item = input('Select (r)ock, (p)aper or (s)cissors: ')
        if user_item == 'r':
            return 'rock'
        elif user_item == 'p':
            return 'paper'
        else:
            return 'scissors'

    @staticmethod
    def get_computer_item():
        items = ['rock', 'paper', 'scissors']
        return random.choice(items)

    @classmethod
    def get_game_result(cls):
        user_item = cls.get_user_item()
        computer_item = cls.get_computer_item()
        print(f'Your item: {user_item}')
        print(f'Computer\'s item: {computer_item}')
        if user_item == computer_item:
            print('You Drew!')
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or (
                user_item == 'paper' and computer_item == 'rock') or (
                user_item == 'scissors' and computer_item == 'paper'):
            print('You Won!')
            return 'win'
        else:
            print('You Lost!')
            return 'loss'


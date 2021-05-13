users = [{
    'username': 'Raz123',
    'password': '123123'
},
    {
        'username': 'Sapirrr',
        'password': 'ABCD'
    },
    {
        'username': 'Moshe10',
        'password': 'M10'
    }
]

logged_in = ''
user_input = ''
while user_input != 'exit':
    user_input = input('Enter a command: ')
    if user_input.lower() == 'login':
        user_name = input('Enter your username: ')
        password = input('Enter your password: ')
        for user in users:
            if user['username'] == user_name and user['password'] == password:
                print('You are now logged in!')
                logged_in = user_name
                break
        if logged_in == '':
            print('Would you like to sign up?: ')
            user_answer = input('Y/N: ')
            if user_answer == 'Y':
                new_dict = {}
                valid = False
                while valid == False:
                    new_user_name = input('Enter a username: ')
                    if not any(d['username'] == new_user_name for d in users):
                        valid = True
                new_password = input('Enter a password: ')
                new_dict['username'] = new_user_name
                new_dict['password'] = new_password
                users.append(new_dict)

print(users)

import psycopg2


def run_sql(query, type='get'):
    HOSTNAME = '127.0.0.1'
    USERNAME = 'postgres'
    PASSWORD = 'Lala1421'
    DATABASE = 'Users_Login'
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    if type == 'get':
        results = cursor.fetchall()
        connection.close()
        return results
    connection.close()



logged_in = ''
user_input = ''
while user_input != 'exit':
    query_of_users = 'select username, password from users'
    users = run_sql(query_of_users, 'get')
    user_input = input('Enter a command: ')
    if user_input.lower() == 'login':
        login_username = input('Enter your username: ')
        login_password = input('Enter your password: ')
        for username, password in users:
            if username == login_username and password == login_password:
                print('You are now logged in!')
                logged_in = username
                break
        if logged_in == '':
            print('Would you like to sign up?: ')
            user_answer = input('Y/N: ')
            if user_answer == 'Y':
                valid = False
                while valid == False:
                    new_user_name = input('Enter a username: ')
                    existing_users = [item for item in users if item[0] == new_user_name]
                    if existing_users == []:
                        valid = True
                new_password = input('Enter a password: ')
                query = f"insert into users(username, password) values ('{new_user_name}','{new_password}')"
                run_sql(query, 'post')


for username, password in users:
    print(username, password)

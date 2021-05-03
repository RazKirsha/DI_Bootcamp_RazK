# Ex1
print('----------------EX1-------------')


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'your balance is now: {self.balance}$')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Cant withdraw that amount!')
        print(f'your balance is now: {self.balance}$')


bank = BankAccount(100)
print(bank.balance)
bank.deposit(20)
bank.withdraw(200)
bank.withdraw(90)
print(bank.balance)

print('-----Part2-----')


class MinimunbalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance=0):
        super().__init__(balance)
        self.minimun_balance = minimum_balance

    def withdraw(self, amount):

        if self.minimun_balance > self.balance - amount:
            self.balance -= amount
        else:
            raise Exception('Cant withdraw that amount!')

        print(f'This is your balance: {self.balance}$')


bank2 = MinimunbalanceAccount(100, -20)
bank2.deposit(20)
# bank2.withdraw(121)
# bank2.withdraw(100)

print('-----Part3-----')


class BankAccount:

    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount):
        if self.authenticated:
            self.balance += amount
            print(f'your balance is now: {self.balance}$')
        else:
            raise Exception('NOT AUTHENTICATED!')

    def withdraw(self, amount):
        if self.authenticated:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print('Cant withdraw that amount!')
            print(f'your balance is now: {self.balance}$')
        else:
            raise Exception('NOT AUTHENTICATED!')

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            print('Authenticated')


bank3 = BankAccount(200, 'Raz', 123123)
# bank3.deposit(100)
bank3.authenticate('Raz', 123123)
bank3.deposit(100)


class ATM:

    def __init__(self, account_list, try_limit=3):
        self.account_list = account_list
        self.try_limit = try_limit
        for al in self.account_list:
            if isinstance(al, BankAccount) or isinstance(al, MinimunbalanceAccount) and try_limit > 3:
                self.valid = True
            else:
                self.valid = False
                raise Exception('NON VALID!')
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while self.current_tries < self.try_limit
            username = input('Enter a username')
            password = input('Enter a password')
            log_in(username, password)
        print('Bye Bye!')

    def log_in(self, username, password):
        for account in self.account_list:
            if username == self.username and password == self.password:
                print('Authenticated')
                show_account_menu()
        else:
           self.current_tries += 1

    def show_account_menu(self):
        using = True
        while using:
            option = input('To deposit')
# Ex 1
print('------Ex1--------')


class PythonBuiltIn:
    """
    This class explores all sorts of dunder methods.
    """

    def __init__(self):
        self.number = -3.12342546
        self.text = ''

    def __abs__(self):
        return abs(self.number)

    def __int__(self):
        return int(self.number)

    def alter_text(self):
        self.text = input('Enter some text: ')
        return self.text


a = PythonBuiltIn()
print(a.number)
print(abs(a))
print(int(a))
print(a.alter_text())

# Ex 2
print('------Ex2--------')


class Currency:

    def __init__(self, coin, value):
        self.coin = coin
        self.value = value

    def __str__(self):
        if self.value > 1:
            return f'{self.value} {self.coin}s'
        return f'{self.value} {self.coin}'

    def __int__(self):
        return self.value

    def __repr__(self):
        if self.value > 1:
            return f'{self.value} {self.coin}s'
        return f'{self.value} {self.coin}'

    def __add__(self, other):
        if isinstance(other, int):
            self.value += other
        elif isinstance(other, Currency):
            if other.coin == self.coin:
                self.value += other.value
            else:
                raise Exception (f'Cannot add between Currency type <{self.coin}> and <{other.coin}>')
        return str(self)


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)

print(str(c1))

print(int(c1))

print(repr(c1))

print(c1 + 5)

print(repr(c1))

print(c1 + c2)


# print(c1 + c3)
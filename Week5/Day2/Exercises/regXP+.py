# Ex1
print('_____________EX1_______________')


class Family:

    def __init__(self, last_name='Cohen'):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        kwargs['age'] = 0
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f'Congratulations for having {kwargs["name"]}')

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    return True
                else:
                    return False


cohens = Family()
cohens.born(name='Bruce', gender='Male')
print(cohens.is_18('Michael'))
print(cohens.members)

# Ex2
print('_____________EX2_______________')


class TheIncredibles(Family):

    def __init__(self):
        self.last_name = 'Parr'
        self.members = [
            {'name': 'Bob',
             'gender': 'Male',
             'power': 'super-strength',
             'incredible_name': 'Mr. Incredible',
             'age': 40
             },
            {'name': 'Hellen',
             'gender': 'Female',
             'power': 'super-stretch',
             'incredible_name': 'Elastigirl',
             'age': 38
             },
            {'name': 'Violet',
             'gender': 'Female',
             'power': 'invisibility, force fields',
             'incredible_name': 'Invisible girl',
             'age': 18
             },
            {'name': 'Dash',
             'gender': 'Male',
             'power': 'super-speed',
             'incredible_name': 'Speedster',
             'age': 15
             }
        ]

    def use_power(self, name):
        if super().is_18(name):
            for member in self.members:
                if member['name'] == name:
                    print(member['power'])
        else:
            print(f'{name} is not over 18')

    def incredible_presentation(self):
        for member in self.members:
            print(f"{member['incredible_name']} ==> {member['power']} ")


inc = TheIncredibles()
inc.use_power('Violet')
inc.incredible_presentation()
inc.born(name='Jack-Jack', incredible_name='Super-Baby', power="Unknown Power")
inc.incredible_presentation()
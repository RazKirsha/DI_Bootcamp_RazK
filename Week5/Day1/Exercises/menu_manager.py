class MenuManager:

    def __init__(self):
        self.menu = [
            {
                'name': 'Soup',
                'price': 10,
                'spice level': 'B',
                'gluten index': False
            },
            {
                'name': 'Hamburger',
                'price': 15,
                'spice level': 'A',
                'gluten index': True
            },
            {
                'name': 'Salad',
                'price': 18,
                'spice level': 'A',
                'gluten index': False
            },
            {
                'name': 'French Fries',
                'price': 5,
                'spice level': 'C',
                'gluten index': False
            },
            {
                'name': 'Beef bourguignon',
                'price': 25,
                'spice level': 'B',
                'gluten index': True
            }
        ]

    def add_item(self, name, price, spice, gluten):
        new_item = {
            'name': name,
            'price': price,
            'spice level': spice,
            'gluten index': gluten
        }
        self.menu.append(new_item)
        print(self.menu)

    def update_item(self, name, price, spice, gluten):
        for meal in self.menu:
            if meal['name'] == name:
                meal['price'] = price
                meal['spice leve'] = spice
                meal['gluten index'] = gluten
                print(self.menu)
                break

        print('There is no such dish in the menu!')

    def remove_item(self, name):
        placeholder = -10
        for index, meal in enumerate(self.menu):
            if name == meal['name']:
                placeholder = index

        if index != 10:
            del self.menu[index]
        else:
            print('There is no such dish in the menu!')

        print(self.menu)


res = MenuManager()
res.add_item('Veggies', 20, 'A', False)
res.update_item('Veggies', 10, 'A', True)
res.remove_item('Veggies')

import json


class MenuManager:

    def __init__(self):
        with open('menu.json', 'r') as f:
            self.menu = json.load(f)

    def add_item(self, name, price):
        print('Now Adding')
        new_item = {
            "name": name,
            "price": price
        }
        self.menu["items"].append(new_item)

    def remove_item(self, name):
        copy_menu = self.menu
        for index, dish in enumerate(copy_menu["items"]):
            if name == dish["name"]:
                del self.menu["items"][index]
                return True
        return False

    def save_to_file(self):
        with open('menu.json', 'w') as f:
            json.dump(self.menu, f, indent=3)

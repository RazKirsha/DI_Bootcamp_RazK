from goldXP import MenuManager


def load_manager():
    new_manager = MenuManager()
    return new_manager


def show_user_menu():
    print('Hello User!')
    user_choice = ' '
    while user_choice != 'a' and user_choice != 'd' and user_choice != 'v' and user_choice != 'x':
        print('MENU')
        print('(a) Add an item')
        print('(d) Delete an item')
        print('(v) View the menu')
        print('(x) Exit')
        user_choice = input()
    return user_choice


def add_item_to_menu(manager):
    user_input_name = input('To add a new dish, Enter a name of a dish')
    user_input_price = int(input('To add a new dish,Enter a price of a dish'))
    manager.add_item(user_input_name, user_input_price)
    print('Item was successfully added')


def remove_item_from_menu(manager):
    user_input_name = input('To remove a dish, Enter a name of a dish')
    if manager.remove_item(user_input_name):
        print('Dish has been removed!')
    else:
        print('Can not remove non-existing dish!')


def show_resturant_menu(manager):
    print(manager.menu["items"])


def exit_prog(manager):
    manager.save_to_file()
    print('Menu was saved successfully')


running = True
manager1 = load_manager()
while running:
    answer = show_user_menu()
    if answer == 'a':
        add_item_to_menu(manager1)
        print(manager1.menu)
    elif answer == 'd':
        remove_item_from_menu(manager1)
    elif answer == 'v':
        show_resturant_menu(manager1)
    elif answer == 'x':
        exit_prog(manager1)
        show_resturant_menu(manager1)
        running = False

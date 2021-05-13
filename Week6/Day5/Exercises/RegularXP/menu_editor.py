from regXP import MenuItem

user_choice = ''
print('Welcome To Mise\'edet Nachos!')
while user_choice != 'q':
    print('select one of the options below: ')
    print('(a)dd an item')
    print('(d)elete an item')
    print('(v)iew the menu')
    print('(q)uit')
    user_choice = input('Enter your choice here: ')

    if user_choice == 'a':
        dish_name = input('Enter a name of a dish: ')
        price = int(input('Enter a price for a dish: '))
        item = MenuItem(dish_name, price)
        item.save()
    elif user_choice == 'd':
        dish_name = input('Enter a name of a dish you would like to delete: ')
        item = MenuItem()
        item.delete(dish_name)
    elif user_choice == 'v':
        MenuItem.all()

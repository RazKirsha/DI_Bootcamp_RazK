topping = 'Placeholder'
toppings = []
price = 10
while topping[0].lower() != 'q':
    topping = input('Pizza what?')
    toppings.append(topping)
    if topping[0].lower() != 'q':
        print(f'We have add a {topping} to your pizza')
        price += 2.5


print(f'price is {price}')

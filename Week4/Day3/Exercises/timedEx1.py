num = int(input("Enter a number"))
all_dividers = 0

for i in range(1, int(num/2)+1):
    if num % i == 0:
        all_dividers += i

if all_dividers == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is  NOT a perfect number')

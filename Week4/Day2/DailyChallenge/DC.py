# Python3 code to calculate age in years
from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) <
    (birthDate.month, birthDate.day))
    return age

# Driver code
# print(calculateAge(date(1997, 2, 3)), "years")

birth_year = int(input("Enter Year of Birth "))
birth_month = int(input("Enter Month of Birth "))
birth_day = int(input("Enter day of Birth "))

age = calculateAge(date(birth_year, birth_month, birth_day))
candles_num = age % 10
dashes_calc = int((18-candles_num)/2)
dashes = '_' * dashes_calc

def cake(candles,dash):
    print('  ' + dash + 'i' * candles + dash + ' ')
    print('  |   :H:a:p:p:y:  |')
    print(' _|________________|_')
    print(' |^^^^^^^^^^^^^^^^^^|')
    print(' | :B:i:r:t:h:d:a:y:|')
    print(' |                  |')
    print(' ~~~~~~~~~~~~~~~~~~~~')

if age % 4 == 0:
    cake(candles_num, dashes)*2
else:
    cake(candles_num, dashes)

# Ex7
from datetime import date
def get_age(day, month, year):
    today = date.today()
    age = today.year - year - ((month, day) < (month, day))
    return age

def can_retire(gender, *date_of_birth):
    age = get_age(*date_of_birth)
    if gender == 'male' and age > 67:
        return True
    elif gender == 'female' and age > 62:
        return True
    else:
        return False

print(can_retire('male',2,7,1958))

# Ex8
def calc(x):
    result = 0
    for i in range(1, 5):
        str_num = str(x)
        nums_str = str_num * i
        result += int(nums_str)
    print(result)

calc(3)
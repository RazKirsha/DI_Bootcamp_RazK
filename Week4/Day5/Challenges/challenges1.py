# Ex1
# list = ['a', 'b', 'C', 1, 2, 4]
# letter = input('What do you wanna enter into the list?')
# index = int(input(f'To where? (from 0 to {len(list)-1})'))
#
# list.insert(index, letter)
#
# print(list)

# Ex2 + 3
string = 'Hello Im Raz and Im a student at DI'
count = string.count(' ')
print(count)
upper_counter = 0
lower_counter = 0


for letter in string:
    if letter.isupper():
        upper_counter += 1
    elif letter.islower():
        lower_counter += 1

print(f'Uppercase letters: {upper_counter}')
print(f'Lowercase letters: {lower_counter}')

# Ex4
def my_sum(*arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)

my_sum(1,2,4)

# Ex5
def find_max(*arr):
    max = min(arr)
    for i in arr:
        if i > max:
            max = i

    print(max)

find_max(1,2,3,5,99,-119,123,21)

# Ex6

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    print(fact)

factorial(4)

# Ex7
def list_count(list,letter):
    counter = 0
    for i in list:
        if i == letter:
            counter += 1
    print(counter)

list_count(['a','a','t','o'],'a')

# Ex8
def norm(list):
    squares = 0
    for num in list:
        squares += num**2
    print(squares**0.5)

norm([1,2,2])

# Ex9
def is_mono(list):

    # new_list.sort()
    print(list)
    new_list = list
    new_list.sort()
    print(list)
    print(new_list)
    # if list == new_list or list == new_list[::-1]:
    #     return True
    # return False

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))

# Ex10
def longest_word(list):
    longest = ''
    for word in list:
        if len(word) > len(longest):
            longest = word

    print(longest)

# Ex11
list = [1,2,3,4,5,'a','adsdfjsd',123,2,'Raz']
strings_list = []
int_list = []
for i in list:
    if type(i) == str:
        strings_list.append(i)
    elif isinstance(i, int):
        int_list.append(i)

print(strings_list)
print(int_list)

# Ex12
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

print(is_palindrome('John'))
print(is_palindrome('radar'))

# Ex13
def sum_over_k(sen, k):
    counter = 0
    list_sen = sen.split()
    for word in list_sen:
        if len(word) > k:
            counter += 1

    print(counter)

sentence = 'Do or do not there is no try'
k = 2
sum_over_k(sentence, k)

# Ex14
dict = {'a': 1,'b':2,'c':8,'d': 1}

def dict_avg(dic):
    counter = 0
    sum = 0
    for i in dic.values():
        counter += 1
        sum += i

    print(sum/counter)

dict_avg(dict)


# Ex15
def common_div(num1, num2):
    div1 = []
    div2 = []
    common_divs = []
    for i in range(2, num1+1):
        if num1 % i == 0:
            div1.append(i)
    for j in range(2, num2+1):
        if num2 % j == 0:
            div2.append(j)

    for k in div1:
        if k in div2:
            common_divs.append(k)

    print(common_divs)

common_div(10,20)

# Ex16
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(11))
print(is_prime(12))

# Ex17
def weird_print(list):
    nums = []
    for index, value in enumerate(list):
        if index % 2 == 0 and value % 2 == 0:
            nums.append(value)

    print(nums)

weird_print([1,2,2,3,4,5])

# Ex18
def type_count(**kwargs):
    integer = 0
    string = 0
    floatie = 0
    boolian = 0
    for key, value in kwargs.items():
        if type(value) == str:
            string += 1
        elif type(value) == int:
            integer += 1
        elif type(value) == float:
            floatie += 1
        elif type(value) == bool:
            boolian += 1
    return {
        'int': integer,
        'str': string,
        'float': floatie,
        'bool': boolian
    }


print(type_count(a=1,b='string',c=1.0,d=True,e=False))

# Ex20

# inputush = "mypassword"
# outputuh = ''
# for letter in inputush:
#     outputuh += '*'

# print(outputuh)


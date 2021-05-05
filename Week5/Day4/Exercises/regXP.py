# Ex1
print('---------Ex1---------')
import random


def get_words_from_file():
    with open('sowpods.txt', 'r') as f:
        return [word[:-2] for word in f]


def get_random_sentence(length):
    words = get_words_from_file()
    sentence = ''
    for i in range(length):
        sentence += random.choice(words).lower() + ' '
    return sentence


def main():
    print('Welcome to the random sentence generator!')
    print('Pick a number between 2 to 20 and enjoy an automated sentence generator')
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        raise Exception('Wrong data type')
    if number > 20 or number < 2:
        raise Exception('number not in requested range!')
    print(get_random_sentence(number))


main()

# Ex2
print('---------Ex2---------')
import json

sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}

with open('json_regXP.json', 'w') as f:
    json.dump(sampleJson, f, indent=3)

with open('json_regXP.json', 'r') as f:
    sample = json.load(f)

print(sample["company"]["employee"]["payable"]["salary"])
sample["company"]["employee"]["birth_date"] = '02071997'
with open('json_regXP.json', 'w') as f:
    json.dump(sample, f, indent=3)

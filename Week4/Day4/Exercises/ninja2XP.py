# Ex1
# def get_full_name(first_name, last_name, middle_name):
#     if middle_name == '':
#         return first_name + ' ' + last_name
#     else:
#         return first_name + ' ' + middle_name + ' ' + last_name
#
# fname = input('first name: ')
# mname = input('middle name: ')
# lname = input('last name: ')
#
# print(get_full_name(fname, lname, mname))

# Ex2
MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(sen):
    '''
    This function Encrypts to morse code
    '''
    word_list = sen.split(' ')
    cypher_code = ''
    for word in word_list:
        for letter in word:
            if letter != ' ':
                cypher_code += MORSE_CODE_DICT[letter.upper()]
                cypher_code += ' '
        cypher_code += '/'
    return cypher_code

def decrypt(morse_sen):
    '''
    This function Decrypts morse code
    '''
    words = morse_sen.split('/')
    decyphered_text = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter != ' ':
                 for key, item in MORSE_CODE_DICT.items():
                     if item == letter:
                         decyphered_text += key
        decyphered_text += ' '
    return decyphered_text

print(decrypt('.... . -.-- /.. -- /.-. .- --.. /'))

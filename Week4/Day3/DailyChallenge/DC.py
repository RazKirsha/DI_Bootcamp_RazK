text = input("Enter a text: ")
question = input("Do you want to decrypt or encrypt?: ")
num = int(input("By How much?: "))
cypher_text = ''

if question[0].lower() == 'e':
     # encryption
     for letter in text:
         # Lowercase letter
         if 97 <= ord(letter) <= 122:
             if ord(letter)+num > 122:
                 cypher_text += chr(ord(letter) + num - 26) # begins one letter before a
             else:
                 cypher_text += chr(ord(letter) + num)
         # Uppercase letters
         elif 65 <= ord(letter) <= 90:
             if ord(letter)+num > 90:
                 cypher_text += chr(ord(letter) + num - 26) # begins one letter before A
             else:
                 cypher_text += chr(ord(letter) + num)

 elif question[0].lower() == 'd':
     # decryption
     for letter in text:
         # Lowercase letter
         if 97 <= ord(letter) <= 122:
             if ord(letter) - num < 97:
                 cypher_text += chr(ord(letter) - num + 26)
             else:
                 cypher_text += chr(ord(letter) - num)
         # Uppercase letters
         elif 65 <= ord(letter) <= 90:
             if ord(letter) - num < 65:
                 cypher_text += chr(ord(letter) - num + 26)
             else:
                 cypher_text += chr(ord(letter) - num)

 print(cypher_text)

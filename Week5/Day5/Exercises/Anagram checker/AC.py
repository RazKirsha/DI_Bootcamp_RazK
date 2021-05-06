class AnagramChecker:

    def __init__(self):
        with open('words.txt', 'r') as f:
            self.all_words = f.read().split('\n')

    def is_valid_word(self, word):
        for text in self.all_words:
            if text == word:
                return True
        return False

    def is_anagram(self, word):
        counter = 0
        anagrams = []
        if self.is_valid_word(word):
            for text in self.all_words:
                for letter in word:
                    if text != word and len(text) == len(word):
                        if letter in text:
                            counter += 1
                        else:
                            break
                if counter == len(word):
                    anagrams.append(text)
                counter = 0
        return anagrams

    # def get_anagrams(self):


# word = 'meat'
# counter = 0
# anagrams = []
# for text in ['hello', 'team', 'bla', 'tea', 'mate', 'sheesh', 'tame']:
#     for letter in word:
#         if text != word and len(text) == len(word):
#             if letter in text:
#                 counter += 1
#             else:
#                 break
#     if counter == len(word):
#         anagrams.append(text)
#     counter = 0
# print(anagrams)

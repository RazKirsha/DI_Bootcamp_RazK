import string
import nltk
from nltk.corpus import stopwords


class Text:

    def __init__(self, text):
        self.text = text

    def count_word(self, word):
        return self.text.count(word)

    def dict_it(self):
        dictio = {}
        text_list = self.text.split(' ')
        for word in text_list:
            if word in dictio.keys():
                dictio[word] += 1
            else:
                dictio[word] = 1

        return dictio

    def most_frequent(self):
        for key, value in self.dict_it().items():
            if value == max(self.dict_it().values()):
                return key

    def uniques(self):
        uniques = []
        for key, value in self.dict_it().items():
            if value == 1:
                uniques.append(key)
        return uniques

    def from_the_stranger(self):
        with open('TheStranger.txt', 'r') as f:
            self.text = f.read()


class TextModification(Text):

    def without_punctuation(self):
        return ' '.join(word.strip(string.punctuation) for word in self.text.split())

    # def remove_stopwords(self):
    #     text_list = [w for w in self.text.split() if w not in (stopwords.words('english'))]
    #     return (' ').join(text_list)

t = Text('Hey Raz my name Raz is Raz Raz')
print(t.count_word('Raz'))
print(t.most_frequent())
print(t.uniques())
t.from_the_stranger()
# print(t.text)
new_t = TextModification('a')
new_t.from_the_stranger()
# print(new_t.without_punctuation())
# print(new_t.remove_stopwords())

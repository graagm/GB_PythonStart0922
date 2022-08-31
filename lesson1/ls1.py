import random

print(random.randint(1,10))

c = random.choices((1, 2, 3, 5, 7), k=3)

f = random.sample((1, 2, 3, 5, 7), k=3)

print(c)
print(f)

class Alphabet:
    def __init__(self, language):
        self.idx = 0
        self.language = language
        if self.language == 'ru':
            self.ls = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        else:
            self.ls = 'abcdefghijklmnopqrstuvwxyz'
        self.n = len(self.ls)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == self.n + 1:
            self.idx = 1
        return self.ls[self.idx - 1]

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
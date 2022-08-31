import random

print(random.randint(1,10))

c = random.choices((1, 2, 3, 5, 7), k=3)

f = random.sample((1, 2, 3, 5, 7), k=3)

print(c)
print(f)
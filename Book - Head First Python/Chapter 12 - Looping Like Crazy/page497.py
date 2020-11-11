from collections import defaultdict

data = [ 1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
print()
print(evens)
print()

evens = [num for num in data if not num % 2]
print()
print(evens)
print()

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print()
print(words)
print()

words = [num for num in data if isinstance(num, str)]

print()
print(words)
print()

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print()
print(title)
print()

title = [word.title() for word in data]

print()
print(title)
print()
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Testing a be be"
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

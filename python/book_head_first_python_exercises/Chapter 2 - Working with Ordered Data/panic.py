phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.remove('t')
plist.remove('p')
plist.insert(3,'t')
plist.extend('p')
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
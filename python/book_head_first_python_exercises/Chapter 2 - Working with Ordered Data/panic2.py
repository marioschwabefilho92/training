phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist = plist[1:8]
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

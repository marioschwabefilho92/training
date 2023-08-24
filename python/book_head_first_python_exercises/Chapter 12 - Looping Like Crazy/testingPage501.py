import pprint

dest = {'9:35': 'FREEPORT',
        '17:00': 'FREEPORT',
        '9:55'	: 'WEST END',
        '19:00': 'WEST END',
        '10:45': 'TREASURE CAY',
        '12:00'	: 'TREASURE CAY',
        '11:45': 'ROCK SOUND',
        '17:55': 'ROCK SOUND'}

print(dest)
pprint.pprint(dest)
print()
print()
print()
new_dic_1 = []
for k, v in dest.items():
    if v == 'WEST END':
        new_dic_1.append(k)

print(new_dic_1)
print()
print()
print()
new_dic_2 = [k for k, v in dest.items() if v == 'WEST END']
print(new_dic_2)
print()
print()
print()
for destination in set(dest.values()):
    print(destination, '->', [k for k, v in dest.items() if v == destination])
print()
print()
print()
new_dic_3 = {}
for destination in set(dest.values()):
    new_dic_3[destination] = [k for k, v in dest.items() if v == destination]
pprint.pprint(new_dic_3)
print()
print()
print()
new_dic_4 = {destination: [k for k, v in dest.items() if v == destination] for destination in set(dest.values())}
pprint.pprint(new_dic_4)
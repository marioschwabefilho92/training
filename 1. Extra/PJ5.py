weight = input('Weight in kg: ')
lbs_or_kg = input('Type L to have it in lbs or type K to have it in kg ')

if lbs_or_kg.upper() == 'L':
    weight = float(weight) * 0.4536
    print(weight)
elif lbs_or_kg.upper() == 'K':
    print(weight)
else:
    print('You typed the incorrect letter')

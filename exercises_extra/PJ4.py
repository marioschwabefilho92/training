price_house = 1000000
good_credit = True

if good_credit:
    price_house = price_house * 0.9
else:
    price_house = price_house * 0.8
print(price_house)

temperature = 35

if temperature > 30:
    print('It is a hot day')
elif temperature <= 30 and temperature >= 10:
    print('It is not so hot')
else:
    print('It is definitely cold')
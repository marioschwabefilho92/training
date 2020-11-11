my_numbers = (4, 5, 3, 9)
print(my_numbers)

#indexes
print(my_numbers[-1])
print(my_numbers[0])

#slices
my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
print(my_numbers[:3])
print(my_numbers[3:])
print(my_numbers[::])
print(my_numbers[1:7:2])

interval = slice(1, 7, 2)
print(my_numbers[interval])

interval = slice(None, 3)
print(my_numbers[interval] == my_numbers[:3])

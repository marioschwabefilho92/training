def f(first, second, third):
    print(first)
    print(second)
    print(third)

l = [1, 2, 3]
f(*l)
# the l is the same as the a, b, c bellow!!!

a, b, c = [1, 2, 3]
f(a, b, c)

# also works for partial!

def show(e, rest):
    print("Element: {0} - Rest: {1}".format(e, rest))

first, *rest = [1, 2, 3, 4, 5]
show(first, rest)

*rest, last = range(6)
show(last, rest)

first, *middle, last = range(6)
print(first)
print(middle)
print(last)
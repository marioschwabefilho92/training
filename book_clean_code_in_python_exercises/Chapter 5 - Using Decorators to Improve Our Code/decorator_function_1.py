def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# Print Hello in UPPERCASE
@uppercase
def greet():
    return 'Hello!'

print(greet())
print(type(greet()))
print(id(greet()))

# Print Hello
def greet():
    return 'Hello!'
    
print(greet())
print(type(greet()))
print(id(greet()))
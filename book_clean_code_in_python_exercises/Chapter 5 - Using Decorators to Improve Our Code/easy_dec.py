from functools import wraps
import functools
import time


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    print(greeter_func)
    return greeter_func("Bob")


# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


# parent()


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

# print(first)
# print(second)
# print(first())
# print(second())


# Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


# say_whee = my_decorator(say_whee)
# print(say_whee)
# say_whee()

# same as new_say_whee = my_decorator(new_say_whee)
@my_decorator
def new_say_whee():
    print("New Whee!")


# print(new_say_whee)
# new_say_whee()


def do_twice(func):
    @wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def say_bye():
    """Print to console Bye Bye"""
    print("Bye Bye")


# print(say_bye)
# say_bye()
# print(say_bye.__name__)
# help(say_bye)


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1000)

import logging
from functools import wraps
import datetime


def log_execution(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logging.info("started execution of %s", function.__qualname__)
        return function(*args, **kwargs)
    return wrapped


def measure_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = function(*args, **kwargs)
        logging.info("function %s took %s", function.__qualname__, start_time)
        return result
    return wrapped


@log_execution
@measure_time
def say_hello():
    """Say Hello There"""
    print("Hello There")


# help(say_hello)
# print(say_hello)
print(say_hello())
print(say_hello.__qualname__)
# print(say_hello.__qualname__)
# print(say_hello.__name__)
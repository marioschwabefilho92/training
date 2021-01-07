# class ControlledExecption(Exception):
#     """A generic exception on the program's domain."""

# def retry(operation):
#     @wraps(operation)
#     def wrapped(*args, **kwargs):
#         last_raised = None
#         RETRIES_LIMIT = 3
#         for _ in range(RETRIES_LIMIT):
#             try:
#                 return operation(*args, **kwargs)
#             except ControlledExecption as e:
#                 logger.info("Retrying %s", operation.__qualname__)
#                 last_raised = e
#         raise last_raised
#     return wrapped

# @retry
# def run_operation(task):
#     """"Run a particular task, simulating some failures on its execution."""
#     return task.run()

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@percent
@star
def printer(msg):
    print(msg)
printer("Hello")
print("")
print("")
print("")

def printer(msg):
    print(msg)
printer = star(percent(printer))

printer("Hello")
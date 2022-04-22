from functools import wraps
from types import MethodType


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"query {query} at {self.dbstring}"


class inject_db_driver:
    """Convert a string to a DBDriver instance and pass this to the wrapped
    function."""

    def __init__(self, function):
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring):
        return self.function(DBDriver(dbstring))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))


class DataHandler:
    @inject_db_driver
    def run_query(self, driver):
        return driver.execute(self.__class__.__name__)


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


print(DataHandler().run_query("test_datahandler"))
print(run_query("test_ok"))

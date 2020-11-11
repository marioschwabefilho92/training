class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

def locate(latitude: float, longitude: float) -> Point:
    """Find an object in the map by its coordinates"""

print(locate.__doc__)
print(locate.__annotations__)

def locate_none(latitude, longitude):
    """Same as locate, but without annotations, but still have doc"""

print(locate_none.__doc__)
print(locate_none.__annotations__)
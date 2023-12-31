# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
        print("this is self temperature "+str(self.temperature))

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    def test_it(self):
        print("Test it also runns")

# create an object
human = Celsius(37)
print(vars(human))
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)
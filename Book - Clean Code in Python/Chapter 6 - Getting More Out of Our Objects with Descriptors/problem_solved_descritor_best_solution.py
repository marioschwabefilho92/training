class DescriptorClass:
    def __init__(self, initial_value):
        self.value = initial_value
        self._name = None
    
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


class ClientClass:
    descriptor = DescriptorClass("first value")


client1 = ClientClass()
print(client1.__dict__)
client2 = ClientClass()
print(client2.__dict__)

client2.descriptor = "Value for the client 2"
print(client2.__dict__)
print(client1.__dict__)

from weakref import WeakKeyDictionary


class DescriptorClass:
    def __init__(self, initial_value):
        self.value = initial_value
        self.mapping = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.mapping.get(instance, self.value)

    def __set__(self, instance, value):
        self.mapping[instance] = value


class ClientClass:
    descriptor = DescriptorClass("first value")


client1 = ClientClass()
print(client1.descriptor)
print(client1.__dict__)
client2 = ClientClass()
print(client2.__dict__)
print(client2.descriptor)

client2.descriptor = "Value for the client 2"
print(client2.descriptor)
print(client2.__dict__)
print(client1.descriptor)
print(client1.__dict__)

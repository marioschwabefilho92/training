class NonDataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

class ClientClass:
    descriptor = NonDataDescriptor()


client = ClientClass()
print(client.descriptor)
client.descriptor = 43
print(client.descriptor)
del client.descriptor
print(client.descriptor)
print(vars(client))
client.descriptor = 99
print(vars(client))
del client.descriptor
print(vars(client))
print(client.descriptor)
client.hatata = 100
print(vars(client))
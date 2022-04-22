class SharedDataDescriptor:
    def __init__(self, initial_value):
        self.value = initial_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value
    

class ClientClass:
    descriptor = SharedDataDescriptor("first value")


client1 = ClientClass()
print(client1.descriptor)

client2 = ClientClass()
print(client2.descriptor)

client2.descriptor = "value for the client 2"
print(client2.descriptor)
print(client1.descriptor)

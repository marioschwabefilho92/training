class DataDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

    def __set__(self, instance, value):
        print("setting %s.descriptor to %s" % (instance, value))
        instance.__dict__["descriptor"] = value


class ClientClass:
    descriptor = DataDescriptor()


client = ClientClass()
print(client.descriptor)
client.descriptor = 99
print(client.descriptor)
print(vars(client))
print(client.__dict__["descriptor"])
del client.descriptor
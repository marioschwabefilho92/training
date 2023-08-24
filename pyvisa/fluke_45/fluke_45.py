import pyvisa as visa

units = visa.ResourceManager().list_resources()
print(units)

resource = visa.ResourceManager().open_resource('GPIB0::10::INSTR')
print(resource)
print(type(resource))
resource.write("*IDN?")
print(resource.read())
import pyvisa as visa 
# rm = visa.ResourceManager('@py')
# print(rm.list_resources())
# print(type(rm.list_resources()))
# print(rm)
# instrument = rm.open_resource("GPIB0::4::INSTR")
# print(instrument)

rm = visa.ResourceManager()
print(rm.list_resources())
print(type(rm.list_resources()))
print(rm)
instrument = rm.open_resource("GPIB0::4::INSTR")
print(instrument)

instrument.read_termination = '\n'
instrument.write_termination = '\n'
instrument.baud_rate = 9600
# print(instrument.write("SYSTEM:KLOCK OFF"))
print(instrument.write("*RST"))
# print(instrument.write("SYSTEM:KLOCK ON"))
# print(instrument.write("*IDN?"))
# print(instrument.query("*IDN?"))
# print(instrument.read())
# instrument.read()
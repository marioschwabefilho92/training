import pyvisa as visa
from time import sleep

units = visa.ResourceManager().list_resources()
print(units)
resource = visa.ResourceManager().open_resource('GPIB0::4::INSTR')
resource.write_termination = '\n'
resource.read_termination = '\n'
resource.baud_rate = 9600
resource.query_delay = 0.5
resource.timeout = 1000
resource.chunk_size = 102400


print(resource.query("*IDN?", delay=3))
# resource.write("*IDN?")
# while True:
#     sleep(10)
#     print(resource.read_bytes(1))

# resource.write("DISP:ENAB ON")
# resource.query("*IDN?")
# resource.write("STAT:OPER:COND?")
# sleep(2)
# print(resource.read_bytes(1))
# print(resource.read())
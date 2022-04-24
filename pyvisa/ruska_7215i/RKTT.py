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

valeus = resource.query_ascii_values('*IDN?')
print(valeus)
from clima_event_c_340_70a_3 import ClimaEvent
import HP34410A
import socket

command_Nr = 99997
chamber_index = 1

addr = '10.128.18.182'
port = 2049
equip = ClimaEvent(addr, port)
temp = equip.get_temperature_value()
temp2 = equip.get_setpoint_temperature_value()
humy = equip.get_humidity_value()
humy2 = equip.get_setpoint_humidity_value()
stop = equip.stop_auto_prg()
# start = equip.start_auto_prg(1,1)
name = equip.get_running_prg_name()
print(temp)
print(temp2)
print(humy)
print(humy2)
print(stop)
# print(start)
print(name)

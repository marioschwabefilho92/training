import cpc6000

print(cpc6000.show_avaliable_cpc6000())
equipment = cpc6000.CPC6000('GPIB0::2::INSTR')
print(equipment.get_idn())
print(equipment.read_baro())
print(equipment.read_pressure())

equipment = cpc6000.CPC6000("TCPIP0::10.128.18.149::49405::SOCKET")
print(equipment.get_idn())
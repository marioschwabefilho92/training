import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources(query='?*::INSTR'))
print(pyvisa.ctwrapper.highlevel.NIVisaLibrary.get_library_paths())
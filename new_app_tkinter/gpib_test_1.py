import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
# import pyvisa
# import ctypes
# ctypes.windll.LoadLibrary(r"C:\Windows\System32\gpib-32.dll")
# rm = pyvisa.ResourceManager('@py')
# print(rm.list_resources())

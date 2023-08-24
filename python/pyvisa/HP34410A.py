import pyvisa as visa


def show_avaliable_resources():
    avaliable_resources = visa.ResourceManager().list_resources()
    filtered_resources = str(avaliable_resources).replace("(", "").replace(")", "").replace("'", "").replace(" ", "").split(",")
    return filtered_resources


class HP34410A:
    range_list = ["AUTO", "MAX", "DEF"] # "MIN" removed
    configuration_list = ["CONFIGURE:VOLTAGE:DC"] # "CONFIGURE:VOLTAGE:AC", "CONFIGURE:RESISTANCE", "CONFIGURE:FRESISTANCE", "CONFIGURE:CURRENT:DC", "CONFIGURE:CURRENT:AC"
    resolution_list = ["MAX"] # "MIN", "DEF" removed

    def __init__(self, visa_address):
        self.resource = visa.ResourceManager().open_resource('%s' % visa_address)

    def get_idn(self):
        self.resource.write("*IDN?")
        return self.resource.read()

    def read(self):
        return self.resource.query('READ?')

    def error(self):
        self.resource.write("SYST:ERR?")
        return self.resource.read()

    def measurement_configuration(self, selected_configuration, selected_range, selected_resolution):
        self.resource.write("%s %s,%s" % (selected_configuration, selected_range, selected_resolution))

import pyvisa as visa


def show_avaliable_agilent_34410a() -> list:
    avaliable_resources = visa.ResourceManager().list_resources()
    filtered_resources = (
        str(avaliable_resources)
        .replace("(", "")
        .replace(")", "")
        .replace("'", "")
        .replace(" ", "")
        .split(",")
    )
    for visa_address in avaliable_resources:
        try:
            resource = Agilent_34410A(visa_address)
            answer = str(resource.get_idn())
            verification = "34410A"
            if (verification in answer) == True:
                pass
            else:
                filtered_resources.remove(visa_address)
        except:
            filtered_resources.remove(visa_address)
    if filtered_resources == []:
        filtered_resources = [""]
    return filtered_resources


class Agilent_34410A:
    range_list = ["AUTO", "MAX", "DEF", "MIN"]
    configuration_list = [
        "CONFIGURE:VOLTAGE:DC",
        "CONFIGURE:VOLTAGE:AC",
        "CONFIGURE:RESISTANCE",
        "CONFIGURE:FRESISTANCE",
        "CONFIGURE:CURRENT:DC",
        "CONFIGURE:CURRENT:AC",
    ]
    resolution_list = ["MAX", "MIN", "DEF"]

    def __init__(self, visa_address):
        self.resource = visa.ResourceManager().open_resource("%s" % visa_address)

    def get_idn(self) -> str:
        """ Read IDN from the device """
        self.resource.write("*IDN?")
        idn = str(self.resource.read())
        return idn

    def read(self) -> float:
        """ Read a value from the device """
        value = float(self.resource.query("READ?"))
        return value

    def error(self) -> str:
        """ Read Error from the device """
        self.resource.write("SYST:ERR?")
        error = str(self.resource.read())
        return error

    def complete_configuration(
        self, selected_configuration, selected_range, selected_resolution
    ) -> bool:
        """ Configures the instrument to measurement type (selected_configuration), range(selected_range) and resolution(selected_resolution) all together. """
        self.resource.write(
            "%s %s,%s" % (selected_configuration, selected_range, selected_resolution)
        )
        return True

    def config_dc_voltage_measurement(self) -> bool:
        """ Configures the instrument to measure voltage DC. """
        self.resource.write("CONFIGURE:VOLTAGE:DC")
        return True

    def config_ac_voltage_measurement(self) -> bool:
        """ Configures the instrument to measure voltage AC. """
        self.resource.write("CONFIGURE:VOLTAGE:AC")
        return True

    def config_dc_current_measurement(self) -> bool:
        """ Configures the instrument to measure current DC. """
        self.resource.write("CONFIGURE:CURRENT:DC")
        return True

    def config_ac_current_measurement(self) -> bool:
        """ Configures the instrument to measure current AC. """
        self.resource.write("CONFIGURE:CURRENT:AC")
        return True

    def config_2w_resistance_measurement(self) -> bool:
        """ Configures the instrument to measure resistance. """
        self.resource.write("CONFIGURE:RESISTANCE")
        return True

    def config_4w_resistance_measurement(self) -> bool:
        """ Configures the instrument to measure 4 wire resistance. """
        self.resource.write("CONFIGURE:FRESISTANCE")
        return True

    def read_configuration(self) -> str:
        """ Read device configuration """
        self.resource.write("CONFIGURE?")
        response = self.resource.read()
        response = response.replace(" ", ",")
        conf = response.split(",")
        conf_string = ""
        conf_string += "Measurement type: " + conf[0] + "\n"
        conf_string += "Range: " + conf[1] + "\n"
        conf_string += "Resolution: " + conf[2]
        return conf_string

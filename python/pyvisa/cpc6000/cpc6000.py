import pyvisa as visa


def show_avaliable_cpc6000() -> list:
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
            resource = CPC6000(visa_address)
            answer = str(resource.get_idn())
            verification = "MENSOR, 600"
            if (verification in answer) == True:
                pass
            else:
                filtered_resources.remove(visa_address)
        except:
            filtered_resources.remove(visa_address)
    if filtered_resources == []:
        filtered_resources = [""]
    return filtered_resources


class CPC6000:
    def __init__(self, visa_address):
        self.resource = visa.ResourceManager().open_resource(visa_address)
        self.resource.read_termination = '\r\n'
        self.resource.write_termination = '\r\n'

    def get_idn(self) -> str:
        """ Read IDN from the device """
        self.resource.write("*IDN?")
        idn = str(self.resource.read())
        return idn

    def read_baro(self) -> float:
        """ Returns reading from barometric sensor"""
        self.resource.write("Baro?")
        value = self.resource.read()
        value = value[1:]
        value = float(value)
        return value

    def read_pressure(self) -> float:
        """ Returns reading from pressure sensor """
        self.resource.write("M$X")
        value = self.resource.read()
        value = value[1:]
        value = float(value)
        return value

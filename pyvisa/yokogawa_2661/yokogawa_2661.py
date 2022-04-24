import pyvisa as visa


def show_avaliable_yokogawa_2661() -> list:
    avaliable_resources = visa.ResourceManager().list_resources()
    filtered_resources = (
        str(avaliable_resources)
        .replace("(", "")
        .replace(")", "")
        .replace("'", "")
        .replace(" ", "")
        .split(",")
    )
    verification = ["KG ","PI ","KP ", "MB ", "HO ", "HG ", "PG ", "PP "]
    for visa_address in avaliable_resources:
        try:
            resource = Yokogawa_2661(visa_address)
            answer = str(resource.read())
            answer = answer[:3]
            if (answer in verification) == True:
                pass
            else:
                filtered_resources.remove(visa_address)
        except:
            filtered_resources.remove(visa_address)
    if filtered_resources == []:
        filtered_resources = [""]
    return filtered_resources

class Yokogawa_2661:

    def __init__(self, visa_address):
        self.resource = visa.ResourceManager().open_resource("%s" % visa_address)

    def read(self) -> str:
        """ Read value from the device """
        value = str(self.resource.read())
        return value

    def unit_change(self, program_data:int):
        """
        Change the measurment based on the integer passed
        0 = kg/cm2 / 1 = psi / 2 = kPa / 3 = mbar / 4 = mmH2O / 5 = mmHg / 6 %(0.2 - 1kg/cm2) / 7 = %(3 - 15psi)
        """
        if program_data < 0 or program_data >  7:
            return "program_data can not be higher than 7 or negative"
        send_str = "UN "+str(program_data)
        self.resource.write(send_str)
        return "Measurement Changed Successfully"

    def turn_on_display(self):
        """Turn on the display"""
        self.resource.write("BD 0")

    def turn_off_display(self):
        """Turn off the display"""
        self.resource.write("BD 1")

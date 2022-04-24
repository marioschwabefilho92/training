import socket
from time import sleep


class ClimaEvent:
    addr = ["10.128.18.182"]
    port = [2049]
    mode = [
        "Temp Check",
        "244LD STD Test",
        "ATE STD Test+Margin",
        "ATE STD Test",
        "ATE Fast",
    ]

    @staticmethod
    def is_valid_length_command_nr(value):
        value = str(value)
        len_value = len(value)
        return len_value == 5

    @staticmethod
    def is_valid_number(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def from_int_to_bytes_ascii(value):
        value = (str(value)).encode("ascii")
        return value

    @staticmethod
    def formated_data(data):
        formated_data = (str(data)).replace("b'1\\xb6", "")
        formated_data = formated_data.replace("\\r\\n'", "")
        return formated_data

    def __init__(self, addr, port):
        self.s = socket.socket()
        try:
            self.s.connect((addr, port))
            self.s.sendall((b"99997\xb61\xb61\r"))
            data = self.s.recv(128)
            print(data)
            formated_data = self.formated_data(data)
            print("Connected to %s with IP %s:%s" % (formated_data, addr, port))
        except:
            print("Could not find ClimeEvent")

    def create_cmd_msg(
        self,
        command_Nr,
        chamber_index,
        argument_1=None,
        argument_2=None,
        argument_3=None,
        argument_4=None,
    ):
        DELIM = b"\xb6"
        CR = b"\r"
        if (
            self.is_valid_length_command_nr(command_Nr) == True
            and self.is_valid_number(command_Nr) == True
        ):
            command_Nr = self.from_int_to_bytes_ascii(command_Nr)
            chamber_index = self.from_int_to_bytes_ascii(chamber_index)
            if (
                argument_1 == None
                and argument_2 == None
                and argument_3 == None
                and argument_4 == None
            ):
                cmd = DELIM.join((command_Nr, chamber_index)) + CR
            elif argument_2 == None and argument_3 == None and argument_4 == None:
                argument_1 = self.from_int_to_bytes_ascii(argument_1)
                cmd = DELIM.join((command_Nr, chamber_index, argument_1)) + CR
            elif argument_3 == None and argument_4 == None:
                argument_1 = self.from_int_to_bytes_ascii(argument_1)
                argument_2 = self.from_int_to_bytes_ascii(argument_2)
                cmd = (
                    DELIM.join((command_Nr, chamber_index, argument_1, argument_2)) + CR
                )
            elif argument_4 == None:
                argument_1 = self.from_int_to_bytes_ascii(argument_1)
                argument_2 = self.from_int_to_bytes_ascii(argument_2)
                argument_3 = self.from_int_to_bytes_ascii(argument_3)
                cmd = (
                    DELIM.join(
                        (command_Nr, chamber_index, argument_1, argument_2, argument_3)
                    )
                    + CR
                )
            elif (
                argument_1 != None
                and argument_2 != None
                and argument_3 != None
                and argument_4 != None
            ):
                argument_1 = self.from_int_to_bytes_ascii(argument_1)
                argument_2 = self.from_int_to_bytes_ascii(argument_2)
                argument_3 = self.from_int_to_bytes_ascii(argument_3)
                argument_4 = self.from_int_to_bytes_ascii(argument_4)
                cmd = (
                    DELIM.join(
                        (
                            command_Nr,
                            chamber_index,
                            argument_1,
                            argument_2,
                            argument_3,
                            argument_4,
                        )
                    )
                    + CR
                )
            else:
                print("Entered argument in invalid order")
        else:
            print("Unknown Error")
        return cmd

    def disconnect_chamber(self):
        self.s.close()

    def get_temperature_value(self):
        cmd = self.create_cmd_msg(11004, 1, 1)
        try:
            self.s.sendall((cmd))
            data = self.s.recv(128)
            formated_data = self.formated_data(data)
            return formated_data
        except:
            print("Not connected to any Chamber")

    def get_setpoint_temperature_value(self):
        cmd = self.create_cmd_msg(11002, 1, 1)
        try:
            self.s.sendall((cmd))
            data = self.s.recv(128)
            formated_data = self.formated_data(data)
            return formated_data
        except:
            print("Not connected to any Chamber")

    def get_humidity_value(self):
        cmd = self.create_cmd_msg(11004, 1, 2)
        try:
            self.s.sendall((cmd))
            data = self.s.recv(128)
            formated_data = self.formated_data(data)
            return formated_data
        except:
            print("Not connected to any Chamber")

    def get_setpoint_humidity_value(self):
        cmd = self.create_cmd_msg(11002, 1, 2)
        try:
            self.s.sendall((cmd))
            data = self.s.recv(128)
            formated_data = self.formated_data(data)
            return formated_data
        except:
            print("Not connected to any Chamber")

    def stop_auto_prg(self):
        cmd = self.create_cmd_msg(19015, 1)
        try:
            rn_prg_name = self.get_running_prg_name()
            self.s.sendall((cmd))
            data = self.s.recv(128)
            if (
                str(data) == "b'1\\r\\n'"
                and rn_prg_name == "Theres is no program running"
            ):
                data = "Program not running"
            elif str(data) == "b'1\\r\\n'" and rn_prg_name != "":
                data = "Program %s stopped" % rn_prg_name
            else:
                data = "Error on stopping test"
            return data
        except:
            print("Not connected to any Chamber")

    def start_auto_prg(self, prog_nr, number_of_executions):
        cmd = self.create_cmd_msg(19014, 1, prog_nr, number_of_executions)
        try:
            rn_prg_name = self.get_running_prg_name()
            if rn_prg_name == "Theres is no program running":
                self.s.sendall((cmd))
                data = self.s.recv(128)
                sleep(1)
                rn_prg_name = self.get_running_prg_name()
                if str(data) == "b'1\\r\\n'" and rn_prg_name != "":
                    data = "Program %s started" % rn_prg_name
                else:
                    data = "Error on starting test"
                return data
            else:
                data = "Program %s is already running" % rn_prg_name
                return data
        except:
            print("Not connected to any Chamber")

    def get_running_prg_name(self):
        cmd = self.create_cmd_msg(19031, 1)
        try:
            self.s.sendall((cmd))
            data = self.s.recv(128)
            formated_data = self.formated_data(data)
            if formated_data == "":
                formated_data = "Theres is no program running"
            else:
                pass
            return formated_data
        except:
            print("Not connected to any Chamber")

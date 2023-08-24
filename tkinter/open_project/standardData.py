import pandas

class DataTable():

    def __init__(self, path):
        self.data = pandas.read_excel(path)

    def locate_string_nummer(self, value:str) -> dict:
        "look into the table on the column Nummer and return the row that matches value"
        result_dict = self.data.loc[self.data["Nummer"].str.contains(value, regex=True)]
        return result_dict

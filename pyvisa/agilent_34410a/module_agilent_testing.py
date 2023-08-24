import agilent_34410A as agi

visa = agi.show_avaliable_resources()
visa = (
    str(visa)
    .replace("(", "")
    .replace(")", "")
    .replace("'", "")
    .replace(" ", "")
    .replace("[", "")
    .replace("]", "")
)
print(visa)
resource = agi.Agilent_34410A(visa)
print(resource.read_configuration())
print(resource.read())

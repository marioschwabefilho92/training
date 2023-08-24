import yokogawa_2661 as yoko 

avaliable_resources = yoko.show_avaliable_yokogawa_2661()
print(avaliable_resources)

resource = yoko.Yokogawa_2661(avaliable_resources[0])
print(resource.read())
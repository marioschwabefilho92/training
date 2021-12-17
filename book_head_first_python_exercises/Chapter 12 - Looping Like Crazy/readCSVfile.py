from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)

print()
flights2 = {}
s = "19:00"
p = convert2ampm(s)
print(p)
print()

for k,v in flights.items():
    flights2[convert2ampm(k)] = v.title()
pprint.pprint(flights2)
print()
print()
more_flights = {convert2ampm(k) : v.title() for k, v in flights.items()}
pprint.pprint(more_flights)
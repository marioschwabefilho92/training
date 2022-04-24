import dec
from base import IDN
import types

agi = dec.doIt

agi.IDN = types.MethodType(IDN, agi)

print(agi)
agi.IDN()
print(agi.IDN)
print(agi.do_this)
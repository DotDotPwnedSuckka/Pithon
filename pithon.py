
from math import sqrt
from decimal import Decimal, getcontext
from time import sleep 
getcontext().prec=100
a = 3405449678154416971853498155008000000 * sqrt(640320)
b = 867407410133324147761288805130794983129
c = a / b
print(c)
sleep(1)
t2 = 2 * c * 6378 
print(t2)

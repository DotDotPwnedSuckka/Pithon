#por arthur sandonato 
from math import sqrt
from decimal import Decimal, getcontext
from time import sleep 
getcontext().prec=100
a = 3405449678154416971853498155008000000 * sqrt(640320)
b = 867407410133324147761288805130794983129
c = a / b
print(c)
sleep(2)
#sessão do cálculo da circunferência da terra
t = c * 12742 #usando o diametro
print(t)
sleep(1)
t2 = 2 * c * 6378 #usando o radio
print(t2)

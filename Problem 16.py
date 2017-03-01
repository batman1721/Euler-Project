#Problem 16

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

import math
import numpy as np

x=2
y=1000
z=math.pow(x, y)
z1=str(long(z))
l=len(z1)
z2=0
z3=0

for i in xrange(0,l):
    z3=z1[i]
    z2=z2+int(z3)

print z2

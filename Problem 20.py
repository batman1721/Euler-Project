#Problem 20
import math

n=math.factorial(100)
comp=len(str(n))
soma=0

for i in xrange(0,len(str(n))):
    soma=soma+int(str(n)[i])

print soma

#Problem 30
import math
soma_total=0

for i in xrange(2,1000000):
    comp=len(str(i))
    soma=0
    for j in xrange(0,comp):
        soma=soma+math.pow(int(str(i)[j]),5)
    if soma==i:
        print soma
        soma_total=soma_total+soma
print soma_total

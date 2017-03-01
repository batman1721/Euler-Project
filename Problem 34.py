#Problem 34
import math
soma_total=0

for i in xrange(3,100000):
    comp=len(str(i))
    soma=0
    for j in xrange(0,comp):
        soma=soma+math.factorial(int(str(i)[j]))
    if soma==i:
        print soma
        soma_total=soma_total+soma
print soma_total

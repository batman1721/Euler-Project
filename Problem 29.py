#Problem 29
import math
a=100
b=100

lista=[]
y=0
for i in xrange(2,a+1):
    for j in xrange(2,b+1):
        x=pow(i,j)
        if (x in lista)==False:
            lista.append(x)
            y=y+1
print y

#Problem 10

from isPrime import isPrime

u=input('Upper limit: ')
s=0

for i in xrange(1,u+1):
    if isPrime(i)==True:
        s=s+i

print s

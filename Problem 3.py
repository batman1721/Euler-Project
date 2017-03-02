#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

n=input('Number: ')

if n%2==0:
    lfactor=2
    n=n/2
    while n%2==0:
        n=n/2
else:
    lfactor=1

factor=3
maxfactor=math.sqrt(n)

while (n>1 and factor<=maxfactor):
    if n%factor==0:
        n=n/factor
        lfactor=factor
        while n%factor==0:
            n=n/factor
        maxfactor=math.sqrt(n)
    factor=factor+2

if n==1:
    print lfactor
else:
    print n

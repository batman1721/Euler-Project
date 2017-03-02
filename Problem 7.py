#Problem 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.
#What is the 10 001st prime number?

from isPrime import isPrime

n=input('Upper Limit: ')
i=0
j=0
while i!=n:
    j=j+1
    if isPrime(j):
        i=i+1

print j

#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from isPrime2 import is_prime
number=input('Number: ')

for i in xrange(number,1,-1):
    if i%2==0:
        pass
    elif number%i==0:
        print i
        if is_prime(i)==True:
            print i
            break

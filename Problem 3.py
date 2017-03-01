#Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number=input('Number: ')

n=number-1
x=number-1
while number%n!=0:
    for i in range(x,2):
       if (x % i) == 0:
           break    
       else:
           n=x
print n

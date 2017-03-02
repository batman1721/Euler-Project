#Problem 5

#2520 is the smallest number that can be divided by
#each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is
#evenly divisible by all of the numbers from 1 to 20?

i=2520

while (i%11!=0 or i%12!=0 or i%13!=0 or i%14!=0 or i%15!=0 or i%16!=0 or i%17!=0 or i%18!=0 or i%19!=0 or i%20!=0):
    i=i+2

print i

# -*- coding: utf-8 -*-
#Problem 6

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first
#ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares
#of the first one hundred natural numbers and the square of the sum.

sqr_sum_small=0
sum_sqr=0
sqr_sum=0
limit=input('limit?' )

for i in xrange (1, limit+1):
    sum_sqr=sum_sqr+i*i
    sqr_sum_small=sqr_sum_small+i
    i+1
sqr_sum=sqr_sum_small*sqr_sum_small

print(sqr_sum-sum_sqr)

# -*- coding: utf-8 -*-
#Problem 14

#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1)
#contains 10 terms. Although it has not been proved yet (Collatz Problem),
#it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

big_k=0
big_coll=0

for x in xrange(13,1000001):
    coll=x
    coll_int=coll
    k=0
    while coll!=1:
        if coll%2==0:
            coll=(coll/2)
            k=k+1
        else:
            coll=(3*coll)+1
            k=k+1
        if k>big_k:
            big_k=k
            big_coll=coll_int

print big_k+1
print big_coll

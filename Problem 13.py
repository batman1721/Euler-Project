#Problem 13

#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
import os
import numpy as np

matr=np.loadtxt('matriz')
matr2=0
for i in xrange(0,100):
    matr2=matr2+np.split(matr,100)[i]

print long(matr2)

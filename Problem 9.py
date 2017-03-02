#Problem 9

import math

for i in xrange(1,500):
    for j in xrange(1,500):
        for k in xrange(1,1000):
            if i+j+k==1000:
                if pow(i,2)+pow(j,2)==pow(k,2):
                    print i*j*k

#Problem 8

from txttostring import txttostring

numbers_file=txttostring('1000.txt')
n=input('numbers in sequence: ')
Y=0

for i in xrange(0,len(numbers_file)-n+1):
    k=1
    for j in xrange(0,n):
        k=k*int(numbers_file[i+j])
    if k>Y:
        Y=k
print Y

# -*- coding: utf-8 -*-
#Problem 27
import math

#Algoritmo que retorna 1 se for primo ou 0 se não for
i=1

def isPrime(n):
    if n==1:
        i=0
    elif n<4:
        i=1
    else:
        if n%2==0:
            i=0
        else:
                if n<9:
                    i=1
                elif n%3==0:
                    i=0
                else:
                   r=math.floor(math.sqrt(n))
                   f=5
                   while f<=r:
                       if n%f==0:
                           i=0
                           break
                       elif n%(f+2)==0:
                           i=0
                           break
                       f=f+6
                       
#Algoritmo de MERDA que só retorna zeros!!!

contagem=0
maxj=0
maxk=0
for j in xrange(1000):
    for k in xrange(1001):
        primos=0
        macacos=1
        while macacos==1:
            for v in xrange(500):
                if isPrime((v^2)+j*v+k)==1:
                    primos=primos+1
                    if primos>contagem:
                        contagem=primos
                        maxj=j
                        maxk=k
                else:
                    macacos=0
print contagem
print maxj
print maxk

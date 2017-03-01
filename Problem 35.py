# -*- coding: utf-8 -*-
#Problem 35

#Algoritmo que testa se são primos
def checkprime(n):
    i = 2
    while True:
        if n==i:
            return True
        if n%i==0:
            return False
        if i*i>n:
            return True
        i = i+1

#Algoritmo em andamento, mas aparenta estar em bom caminho
for j in xrange(71,1000000):
    k=checkprime(j)
    if k==True:
        if len(str(j))==2:
            if checkprime(int(str(j)[1]+str(j)[0]))==True:
                print j
        elif len(str(j))==3:
            if checkprime(int(str(j)[1]+str(j)[0]+str(j)[2]))==True:
                if checkprime(int(str(j)[2]+str(j)[0]+str(j)[1]))==True:
                    if checkprime(int(str(j)[0]+str(j)[2]+str(j)[1]))==True:
                        print j
        else:
            if checkprime(int(str(j)[1]+str(j)[0]+str(j)[2]+str(j)[2:]))==True:
                if checkprime(int(str(j)[2]+str(j)[0]+str(j)[1]+str(j)[2:]))==True:
                    if checkprime(int(str(j)[0]+str(j)[2]+str(j)[1]+str(j)[2:]))==True:
                        if checkprime(int(str(j)[::-1]))==True:
                            j1=str(j)[::-1]
                            if checkprime(int(j1[1]+j1[0]+j1[2]+j1[2:]))==True:
                                print j

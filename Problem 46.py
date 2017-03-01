import math

primos = open("primos.txt","r")
primos=primos.read()
primos1=[]
intermedio=''
for i in xrange(0,len(primos)-1):
    if primos[i]==' ':
        primos1.append(int(intermedio))
        intermedio=''
    else:
        intermedio=intermedio+str(primos[i])

def primo_prox(x):
    for i in xrange(0,len(primos1)-1):
        if primos1[i]==x:
            return i
            break
        elif primos1[i]>x:
            return i-1
            break


def soma_goldbach(x):
    resultado=0
    y=primo_prox(x)
    for i in xrange(0,20):
        for j in xrange(0,500):
            resultado=primos1[y-j]+2*math.pow(i,2)
            if resultado==x:
                break
                break
    if resultado==0:
        print x



for u in xrange(9,1000,2):
    if u not in primos1:
        soma_goldbach(u)

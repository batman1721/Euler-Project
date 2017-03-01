# -*- coding: utf-8 -*-
#Problem 54

#Algoritmo que transforma o p054_poker.txt em 2 listas
#p11 e p22, sendo assim possível comparar mãos numa mesma
#ronda (print p11[1] e print p22[1]) ou mesmo carateres de
#uma mão (print p11[1][1])


def abrir(x):
    with open(x) as f:
        linha = f.readlines()
    p11=[]
    p22=[]
    p1=''
    p2=''
    for i in xrange(0,1000):
        for j in xrange(0,29):
            if j<=13:
                p1=p1+linha[i][j]
            elif j>=15:
                p2=p2+linha[i][j]
        p11.append(p1)
        p22.append(p2)
        p1=''
        p2=''
    p=[]
    p.append(p11)
    p.append(p22)
    return p

#Função que verifica o Royal Flush numa dada mão
#x será igual a p11[...] ou p22[...]

def royal(x):
    if ('A' in x) and ('K' in x) and ('Q' in x) and ('J' in x) and ('T' in x):
        return True
        
def flush(x):
    if x[1]==x[4] and x[1]==x[7] and x[1]==x[10] and x[1]==x[13]:
        return True

#def straight(x):
#    if
#        STRAIGHT 5

def royal_flush(x):
    if flush(x)==True:
        if royal(x)==True:
            #value=10
            return True

def poker(x):
    if x[0]==x[3] and x[0]==x[6] and x[0]==x[9]:
        #value=8
    elif x[3]==x[6] and x[3]==x[9] and x[3]==x[12]:
        #value=8
    return True

def straight_flush(x):
    if flush(x)==True:
        if straight(x)==True:
            #value=9
            return True

#def pair(x):
#PAIR 2

#def two_pair(x):
#TWO Pair 3

#def high_card(x):
#HIGH CARD 1

#def trio(x):
#TRIO 4

#def full_house(x):
#    if trio(x)==True:
#        if #PAR QUE NÃO PERTENÇA AO TRIO:
#            FULL HOUSE 7


#Algoritmo que faz a comparação das mãos
#def comparar(x,y):




ficheiro='p054_poker.txt'
ficheiro=abrir(ficheiro)
print ficheiro[0][0]

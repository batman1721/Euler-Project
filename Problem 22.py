# -*- coding: utf-8 -*-
#Problem 22

#Ler ficheiro
with open('p022_names.txt','r') as n:
    nomes_raw= n.read().lower()
#Por nome em cada linha e remover vírgula
nomes_raw=nomes_raw.replace(',','\n')
#Remover aspas
nomes_raw=nomes_raw.replace('"','')
#Listar cada linha como objeto de uma lista
nomes=nomes_raw.split()
#Ordenar
nomes.sort()

total=0
cont=0

for i in xrange(0,len(nomes)):
    cont=0
    for j in xrange(0,len(nomes[i])):
        if nomes[i][j]=='a':
            cont=cont+1
        elif nomes[i][j]=='b':
            cont=cont+2
        elif nomes[i][j]=='c':
            cont=cont+3
        elif nomes[i][j]=='d':
            cont=cont+4
        elif nomes[i][j]=='e':
            cont=cont+5
        elif nomes[i][j]=='f':
            cont=cont+6
        elif nomes[i][j]=='g':
            cont=cont+7
        elif nomes[i][j]=='h':
            cont=cont+8
        elif nomes[i][j]=='i':
            cont=cont+9
        elif nomes[i][j]=='j':
            cont=cont+10
        elif nomes[i][j]=='k':
            cont=cont+11
        elif nomes[i][j]=='l':
            cont=cont+12
        elif nomes[i][j]=='m':
            cont=cont+13
        elif nomes[i][j]=='n':
            cont=cont+14
        elif nomes[i][j]=='o':
            cont=cont+15
        elif nomes[i][j]=='p':
            cont=cont+16
        elif nomes[i][j]=='q':
            cont=cont+17
        elif nomes[i][j]=='r':
            cont=cont+18
        elif nomes[i][j]=='s':
            cont=cont+19
        elif nomes[i][j]=='t':
            cont=cont+20
        elif nomes[i][j]=='u':
            cont=cont+21
        elif nomes[i][j]=='v':
            cont=cont+22
        elif nomes[i][j]=='w':
            cont=cont+23
        elif nomes[i][j]=='x':
            cont=cont+24
        elif nomes[i][j]=='y':
            cont=cont+25
        elif nomes[i][j]=='z':
            cont=cont+26
    total=total+cont*(i+1)

print total

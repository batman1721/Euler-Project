#Problem 18

triangulo=[]
n_triangulo=[]
variavel1=[]
variavel2=[]
triangulo2=[]
n_index=[]
with open('Problem_18.txt') as f:
    for i in xrange(0,15):
        triangulo.append(f.readline())

def converter(x):
    for i in xrange(0,len(x)):
        n_triangulo.append(i)
        variavel1=[]
        for j in xrange(0,len(x[i])-2,3):            
            variavel1.append(int(x[i][j]+x[i][j+1]))
            #variavel2.append(j)
        n_triangulo[i]=variavel1
        #n_index[i]=variavel2
    return n_triangulo

def ordenado(x):
    q=0
    for i in xrange(0,len(x)-1):
        if x[i]<x[i+1]:
            q=1
    if q==1:
        return False
    else:
        return True

def criar_n_index(x):
    for i in xrange(0,len(x)):
        n_index.append(i)
        variavel2=[]
        for j in xrange(0,len(x[i])):
            variavel2.append(j)
        n_index[i]=variavel2
    return n_index

def ordenar(x,y):
    i=0
    while ordenado(x)==False:
        if i==len(x)-1:
            i=0
        else:
            if x[i]<x[i+1]:
                u=y[i]
                y[i]=y[i+1]
                y[i+1]=u
                p=x[i+1]
                x[i+1]=x[i]
                x[i]=p 
                i=i+1
            else:
                i=i+1
    return x

w=converter(triangulo)
t=criar_n_index(w)
for i in xrange(0,len(w)):
    triangulo2.append(ordenar(w[i],t[i]))
## Ate aqui apenas cria, ordena e formata as variaveis de maneira
## a serem de mais facil acesso

soma=75
k=0
for i in xrange(1,len(w)):
    for j in xrange(0,len(t[i])):
        if t[i][j]==0 and t[i][j]==k:
            k=t[i][j]
            soma=soma+w[i][j]
            break
        elif t[i][j]==k or (t[i][j])==k+1:
            k=t[i][j]
            soma=soma+w[i][j]
            break
print soma

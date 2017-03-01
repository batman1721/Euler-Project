#Problem 121

itera=20
n_vermelho=[]
n_azul=[]

def n_prob_a_v(x):
    p=1
    for i in xrange(2,x+2):
        n_v=float(1)/i
        n_vermelho.append(n_v)
        n_a=float(p)/i
        n_azul.append(n_a)
        p=p+1

n_prob_a_v(itera)

def probab_apenas_um(x):
    k=1
    for i in xrange(0,len(x)):
        k=k*x[i]
    return k

                    

print probab_apenas_um(n_vermelho)
print probab_apenas_um(n_azul)

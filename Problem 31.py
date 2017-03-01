#Esta muito lento!!


quantia=200

valores=(1,2,5,10,20,50,100,200)
max_val=(quantia/valores[0],quantia/valores[1],quantia/valores[2],quantia/valores[3],quantia/valores[4],quantia/valores[5],quantia/valores[6],quantia/valores[7])

max_val_a=[]
for i in xrange(0,8):
    if max_val[i]!=0:
        max_val_a.append(max_val[i])
    else:
        max_val_a.append(0)
        
def combinacao(x,y,z,xx,yy,zz,xxx,yyy):
    combin=[]
    combin.append(x)
    combin.append(y)
    combin.append(z)
    combin.append(xx)
    combin.append(yy)
    combin.append(zz)
    combin.append(xxx)
    combin.append(yyy)
    return combin

#x e a quantia ,y e a combinacao e z os valores de cada moeda
def valido(x,y,z):
    soma=0
    for i in xrange(0,8):
        soma=soma+y[i]*z[i]
    if soma==x:
        return True
    else:
        return False


MANEIRAS=0   
for i in xrange(0,max_val_a[0]):
    for j in xrange(0,max_val_a[1]):
        for k in xrange(0,max_val_a[2]):
            for ii in xrange(0,max_val_a[3]):
                for jj in xrange(0,max_val_a[4]):
                    for kk in xrange(0,max_val_a[5]):
                        for iii in xrange(0,max_val_a[6]):
                            for jjj in xrange(0,max_val_a[7]):
                                if valido(quantia,combinacao(i,j,k,ii,jj,kk,iii,jjj),valores):
                                    MANEIRAS=MANEIRAS+1

print MANEIRAS

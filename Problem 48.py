#Problem 48

soma=0

for i in xrange(1,1001):
    soma=soma+pow(i,i)

soma_str=str(soma)
print soma_str[-10:]

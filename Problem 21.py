#Problem 21

def s_divisors(n):
    soma=0
    for i in xrange(1,n):
        if n%i==0:
            soma=soma+i
    return soma

def amicables(n):
    u=0
    u=s_divisors(n)
    if s_divisors(u)==n and n!=u:
        return True

cont=0
cont2=0
for j in xrange(1,10001):
    if amicables(j)==True:
        cont=cont+s_divisors(j)
        if s_divisors(j)>10001:
            cont2=cont2+1

print cont-cont2

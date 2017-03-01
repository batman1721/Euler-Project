#Problem 12 - PRECISA DE MAIOR RAPIDEZ!

#The sequence of triangle numbers is generated by adding the natural numbers.
#So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#The first ten terms would be:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#Let us list the factors of the first seven triangle numbers:
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over
#five hundred divisors?

raio=100000000 #Qualquer valor grande suficiente para ser quebrado no "break"
cont=0

def n_divisores(x):
    n=0
    for i in xrange(1,x+1):
        if (x%i)==0:
            n=n+1
    return n

for i in xrange(1,raio):
    cont=cont+i
    if n_divisores(cont)>5:
        break

print cont

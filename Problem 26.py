#Problem 26

d=10

def ciclo(x):
    top=0
    for i in xrange(2,4):
        if x[i]==x[i+1] and x[i]==x[i+2] and x[i]==x[i+3]:
            top=1
        elif x[i]==x[i+2] and x[i]==x[i+4]:
            top=2
        elif x[i]==x[i+3] and x[i]==x[i+6]:
            top=3
        elif x[i]==x[i+4] and x[i]==x[i+8]:
            top=4
        elif x[i]==x[i+5] and x[i]==x[i+10]:
            top=5
        elif x[i]==x[i+6] and x[i]==x[i+12]:
            top=6
    return top        
        


maior=0
for i in xrange(2,d):
    if ciclo(str(float(1)/d))>maior:
        maior=ciclo(float(1)/d)

print maior

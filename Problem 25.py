#Problem 25

i=2
fu=[]
fu.append(1)
fu.append(1)

while len(str(fu[i-1]))<1000:
    fu.append(fu[i-1]+fu[i-2])
    i=i+1
print i
print fu[i-1]

#Problem 40

decimal=''
for i in xrange(1,1000000):
    decimal=decimal+str(i)

conta=int(decimal[0])*int(decimal[9])*int(decimal[99])*int(decimal[999])*int(decimal[9999])*int(decimal[99999])*int(decimal[999999])
print conta

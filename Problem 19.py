#Problem 19

#You are given the following information, but you may prefer to do
#some research for yourself.
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month
#during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

lista=[]

for ano in xrange(1901,2001):
    for mes in xrange(1,13):
        if mes==4 or mes==6 or mes==9 or mes==11:
            for dia in xrange(1,31):
                lista.append(ano)
                lista.append(mes)
                lista.append(dia)
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            for dia in xrange(1,32):
                lista.append(ano)
                lista.append(mes)
                lista.append(dia)
        elif mes==2:
            if (ano%4==0 and ano%100!=0) or ano%400==0:
                for dia in xrange(1,30):
                    lista.append(ano)
                    lista.append(mes)
                    lista.append(dia)
            else:
                for dia in xrange(1,29):
                    lista.append(ano)
                    lista.append(mes)
                    lista.append(dia)


n_domingos=0
indices=[]
domingos_no_um=0

for i in xrange(2,len(lista),3*7):
    n_domingos=n_domingos+1
    indices.append(i)
    
for j in xrange(0,len(indices)):
    if lista[indices[j]]==1:
        domingos_no_um=domingos_no_um+1

print domingos_no_um

# -*- coding: utf-8 -*-
#Problem 17

#If the numbers 1 to 5 are written out in words:
#one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
#letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive
#were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens.For example, 342
#(three hundred and forty-two) contains 23 letters and 115
#(one hundred and fifteen) contains 20 letters.
#The use of "and" when writing out numbers is in compliance with British usage.

#Números entre 1 e 9
def numb9(x):
    if x==2 or x==6 or x==1:
        return 3
    elif x==3 or x==8 or x==7:
        return 5
    elif x==9 or x==4 or x==5:
        return 4
    elif x==0:
        return 0
def numb99(x):
    if x==2 or x==3 or x==8 or x==9:
        return 6
    elif x==5 or x==6 or x==4:
        return 5
    elif x==7:
        return 7
    elif x==0:
        return 0

def numb19(x):
    if x==10:
        return 3
    elif x==11 or x==12:
        return 6
    elif x==14 or x==13 or x==18 or x==19:
        return 8
    elif x==15 or x==16:
        return 7
    elif x==17:
        return 9

count=0

for number in xrange(1,1001):

#Números entre 1 e 9
    if number<10:
        count=count+numb9(number)
#Número 1000
    elif number==1000:
        count=count+8+3

#Números entre 10 e 19
    elif number>9 and number<20:
        count=count+numb19(number)

#Números entre 20 e 99
    elif number<100 and number>19:
        i=int(number/10)
        count=count+numb99(i)
        j=(number-(i*10))
        count=count+numb9(j)


#Números entre 100 e 999
    elif (number>=100 and number<=999):
        print number
        k=int(number/100)
        count=count+numb9(k)+7
        
        i=(number-(k*100))
        if i>9 and i<20:
            count=count+numb19(i)+3
        else:
            count=count+numb99(i)+3            
        j=(number-(k*100)-(i*10))
        count=count+numb9(j)

print count

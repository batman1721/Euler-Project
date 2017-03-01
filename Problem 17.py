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

count=0

for number in xrange(1,1001):

#Números entre 20 e 99
    if number<100 and number>19:
        i=number
        i=int(i/10)
    
        if i==2 or i==3 or i==8 or i==9:
            count=count+6
        elif i==5 or i==6 or i==4:
            count=count+5
        elif i==7:
            count=count+7
    
        j=(number-(i*10))
    
        if j==1 or j==2 or j==6:
            count=count+3
        elif j==3 or j==7 or j==8:
            count=count+5
        elif j==4 or j==5 or j==9:
            count=count+4
        print number
        print count
#Números entre 100 e 999
    elif (number>=100 and number<110) or (number>119 and number<210) or (number>219 and number<310) or (number>319 and number<410) or (number>419 and number<510) or (number>519 and number<610) or (number>619 and number<710) or (number>719 and number<810) or (number>819 and number<910) or (number>919 and number<1000):
        k=number
        k=int(k/100)
        
        if k==2  or k==6 or k==1:
            count=count+3+7+3
        elif k==5 or k==9 or k==4:
            count=count+4+7+3
        elif k==7 or k==8 or k==3:
            count=count+5+7+3
        
        i=(number-(k*100))
        i=int(i/10)

        if i==2 or i==3 or i==8 or i==9:
            count=count+6
        elif i==5 or i==6 or i==4:
            count=count+5
        elif i==7:
            count=count+7
            
        j=(number-(k*100)-(i*10))

        if j==1 or j==2 or j==6:
            count=count+3
        elif j==3 or j==7 or j==8:
            count=count+5
        elif j==4 or j==5 or j==9:
            count=count+4
        print number
        print count
#Números entre 1 e 9
    elif number <10:
        i=number
        if i==2 or i==6 or i==1:
            count=count+3
        elif i==3 or i==8 or i==7:
            count=count+5
        elif i==9 or i==4 or i==5:
            count=count+4
        print number
        print count
#Números entre 10 e 19
    elif number>9 and number<20:
        i=number

        if i==10:
            count=count+3
        elif i==11 or i==12:
            count=count+6
        elif i==14 or i==13 or i==18 or i==19:
            count=count+8
        elif i==15 or i==16:
            count=count+7
        elif i==17:
            count=count+9
        print number
        print count    
#Números entre 111 e 119
    elif (number>=110 and number<=119) or (number>=310 and number<=319) or (number>=410 and number<=419) or (number>=510 and number<=519) or (number>=610 and number<=619) or (number>=710 and number<=719) or (number>=810 and number<=819) or (number>=210 and number<=219) or (number>=910 and number<=919):
        i=number
        i=int(i/100)
        
        if i==2  or i==6 or i==1:
            count=count+3+7
        elif i==5 or i==9 or i==4:
            count=count+4+7
        elif i==7 or i==8 or i==3:
            count=count+5+7   

        j=(number-(i*100))
        if j==10:
            count=count+3
        elif j==11 or j==12:
            count=count+6
        elif j==14 or j==13 or j==18 or j==19:
            count=count+8
        elif j==15 or j==16:
            count=count+7
        elif j==17:
            count=count+9
        print number
        print count
#Número 1000
    elif number==1000:
        count=count+8+3
        print number
        print count
print count

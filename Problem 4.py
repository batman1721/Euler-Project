# -*- coding: utf-8 -*-
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


n=0
ii=0
jj=0

for i in xrange(100,999):
    for j in xrange(100,999):
        num=j*i
        reverse = 0                             #Algoritmo de reversão da variável
        number=num                              #
        while(number > 0):                      #
            reminder = number %10               #
            reverse = (reverse *10) + reminder  #
            number = number //10                #
            if reverse==num and num>n:          #Comparar reversão com original
                n=num                           #e substituir caso seja maior
                ii=i                            #
                jj=j                            #
print n

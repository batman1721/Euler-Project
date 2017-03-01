# Problem 1

# If we list all the natural numbers below 10
#that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

n=0
upper_limit=input('What is the upper limit? ')

for i in xrange(1,upper_limit):
    if i%3==0 or i%5==0:
        n=n+i

print 'The sum of all the multiples of 3 or 5 below %d is %d' %(upper_limit,n)

#Problem 24

import itertools

permutas=list(itertools.permutations('0123456789'))
permutas.sort

print permutas[999999]

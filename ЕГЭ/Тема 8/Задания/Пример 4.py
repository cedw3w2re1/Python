import itertools
from itertools import product
n=0
n1 = '13579'
n2 = '02468'

list_v = itertools.product(n1,n2,n1,n2)

for str in list_v:
    line = ''.join(str)
    if line[0] != '0' and line[0] != line[2] and line[1] != line[3]:
        n+=1

list_v = itertools.product(n2,n1,n2,n1)

for str in list_v:
    line = ''.join(str)
    if line[0] != '0' and line[0] != line[2] and line[1] != line[3]:
        n+=1
print(n)
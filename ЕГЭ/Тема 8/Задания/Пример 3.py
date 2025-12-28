import itertools
from itertools import product
n = 1

list_v = itertools.product('АПРСУ', repeat = 5)

for str in list_v:
    line = ''.join(str)
    if line.count('У') <= 1 and line.count('АА') == 0:
        print(n, line)
    n+=1
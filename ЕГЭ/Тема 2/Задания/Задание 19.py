# Решение

from itertools import product

print('u x y z w')
for u, x, y, z, w in product([0, 1], repeat=5):
    if not(((x <= y) and (z == (not(w)))) <= (u == (x or z))  ):
        print(u,x,y,z,w)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 19, answer, 'b83215ff76ddd410e32571919b78d0eb'))
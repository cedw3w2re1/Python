from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not((x == (not(y))) <= ((x and w) == (z and not(w)))):
        print(x,y,z,w)
# Решение
from itertools import product, permutations


def f1(x, y, z, w):
    return (x or not(y)) <= (w == z )


def f2(x, y, z, w):
    return (x or not(y)) == (w <= z)


for x1, x2, x3, x4, x5,x6 in product([0, 1], repeat=6):
    table = [
        (0, x1, 0, 0) + (0, 0),
        (x2, 1, 1, x3) + (0, x4),
        (x5, 0, 0, 0) + (x6, 0)
    ]
    # Проверка на то, что в таблице не повторяются строки
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, s))) == s[-2] and f2(**dict(zip(p, s))) == s[-1] for s in table):
                print(p)






answer = ywxz

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 11, answer, '7379de4777f5748aa568b8d0bf8c3795'))
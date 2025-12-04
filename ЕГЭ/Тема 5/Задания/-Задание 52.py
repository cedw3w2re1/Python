# Решение


def f(n):
    s1 = 0
    s0 = 0
    b = bin(n)[2:]
    for i in range(len(b)):
        if i % 2 == 0 and b[i] == '1':
            s1 += 1
        elif i % 2 != 0 and b[i] == '0':
            s0 += 1
    return abs(s1 - s0) == 5

n = 1
while True:
    if f(n):
        print(n)
        break
    n += 1



answer = 511

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))
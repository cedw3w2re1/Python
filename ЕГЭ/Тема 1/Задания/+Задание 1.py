# Решение
from itertools import permutations

table = '13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76'
graph = 'AB AF AG GD GF DF DC CF FE FB BE BA FA GA DG FG FD CD FC EF BF EB'

for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)






answer = 67

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 1, answer, '735b90b4568125ed6c3f678819b6e058'))


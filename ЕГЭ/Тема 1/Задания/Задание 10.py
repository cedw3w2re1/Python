# Решение
from itertools import permutations

table = '346 3478 1248 1236 678 1457 2568 2568 2357'
graph = 'AБ БИ БВ БД АВ АГ АЖ ГЕ ВД ДИ ИЖ ИЕ ДЕ'

for p in permutations('АБВГДИЖЕ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)




answer = ...

#


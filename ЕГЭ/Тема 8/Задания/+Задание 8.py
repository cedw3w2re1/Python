# Решение
import itertools

list_v = itertools.product('ГЕПАРД', repeat = 5)
n = 0

for str in list_v:
    line = ''.join(str)
    if line.count('Г') == 1 and line[0] != 'А' and line[-1] != 'Е':
        n += 1
print(n)







answer = 2200

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 8, answer, '5249ee8e0cff02ad6b4cc0ee0e50b7d1'))
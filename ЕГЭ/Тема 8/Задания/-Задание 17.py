# Решение
import itertools
n = 0
n1 = '02468'
n2 = '13579'

list_v = itertools.product(n1,n2,n1,n2,n1,n2,n1,n2,n1,n2,n1)

for str in list_v:
    line = ''.join(str)
    if line[0] != '0' and line[0] != line[2] and line[1] != line[3] and line.count('1') <= 4 and line.count('0') <= 4 and line.count('1') <= 4 and line.count('2') <= 4 and line.count('3') <= 4 and line.count('4') <= 4 and line.count('5') <= 4 and line.count('6') <= 4 and line.count('7') <= 4 and line.count('8') <= 4 and line.count('9') <= 4:
        n+=1




print(n*2)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))
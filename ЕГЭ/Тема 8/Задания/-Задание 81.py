# Решение
import itertools

list_v = itertools.product('РОРОРАРА', repeat = 8)
n = 0

for str in list_v:
    line = ''.join(str)
    if line.count('Р') == 3 and line.count('О') == 2 and line.count('А') == 2 and line.count('РР') == 0 and line.count('ОО') == 0 and line.count('АА') == 2 :
        n += 1
print(n)






answer = 161280

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))
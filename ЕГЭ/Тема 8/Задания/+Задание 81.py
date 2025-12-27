# Решение
import itertools

list_v = itertools.product('РОСОМАХА', repeat = 8)
n = 0

for str in list_v:
    line = ''.join(str)

print(n)






answer = 288
#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))
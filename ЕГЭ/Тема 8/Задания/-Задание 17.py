# Решение
import itertools

n = 0
for str in itertools.product('12', repeat=11):
    s = ''.join(str)
    if s[0] == '1' and '22' not in s:
        n += 1
print(n)





answer = 144

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))
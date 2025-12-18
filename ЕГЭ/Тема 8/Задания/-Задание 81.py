from itertools import *
k=0
for al,a2,a3,a4,a5,a6 in product('РУРРАР',repeat=6):
    s = al+a2+a3+a4+a5+a6
# если в итоговой строке 3 и более букв Р,
# то в строке без замен было бы три согласных
    if s.count('P')>=3:
        k = k + 1
print (k)


answer = 49152

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))
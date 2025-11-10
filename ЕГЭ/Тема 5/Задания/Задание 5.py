# Решение
def f(n):
    b = bin(n)[2:]
    b = b.replace("0", '*')
    b = b.replace("1", '0')
    b = b.replace("*", '1')
    return int(b, 2)

if n-b == 999:
    print(n)







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))
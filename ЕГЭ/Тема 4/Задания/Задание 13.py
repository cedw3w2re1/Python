answer = ...


import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '698d51a19d8a121ce581499d7b701668' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 13, 4, result)

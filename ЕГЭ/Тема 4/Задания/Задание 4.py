answer = ...


import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == 'c74d97b01eae257e44aa9d5bade97baf' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 4, 4, result)

# Решение

from turtle import *
tracer(0)
k = 20


for i in range(2):
    fd(3*k)
    lt(90)
    bk(10*k)
    lt(90)
up()

bk(10*k)
rt(90)
fd(8*k)
lt(90)

down()

for i in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)
up()
for x in range(-k,k):
    for y in range(-k,k):
        goto(x*k, y*k)
        dot(3)
exitonclick()



answer = 44

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))










